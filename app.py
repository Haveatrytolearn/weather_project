"""
Flask web application for Weather Project.
Provides a beautiful interface to analyze weather data.
"""

from datetime import datetime
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from weather import load_data_from_csv, generate_summary, generate_daily_summary

app = Flask(__name__)
DATA_DIR = "tests/data"
UPLOAD_DIR = "uploaded_data"
ALLOWED_EXTENSIONS = {"csv"}

os.makedirs(UPLOAD_DIR, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_available_files():
    """Get list of available CSV files from sample and uploaded folders."""
    files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
    uploads = [f for f in os.listdir(UPLOAD_DIR) if f.endswith('.csv')]
    return sorted(files + uploads)


def get_file_source(filename):
    upload_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(upload_path):
        return "uploaded"
    return "sample"


def get_upload_date(filename):
    filepath = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(filepath):
        return None
    timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def build_response(filename, weather_data):
    return {
        'days': len(weather_data),
        'summary': generate_summary(weather_data),
        'daily_summary': generate_daily_summary(weather_data),
        'filename': filename,
        'source': get_file_source(filename),
        'upload_date': get_upload_date(filename)
    }


@app.route('/')
def index():
    """Home page with file selection."""
    files = get_available_files()
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload a new CSV file and analyze it immediately."""
    if 'weather_file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['weather_file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Only CSV files are allowed'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_DIR, filename)
    file.save(filepath)

    try:
        weather_data = load_data_from_csv(filepath)
        if not weather_data:
            return jsonify({'error': 'File is empty or invalid'}), 400

        files = get_available_files()
        response = build_response(filename, weather_data)
        response['files'] = files
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/delete', methods=['POST'])
def delete_file():
    """Delete an uploaded CSV file."""
    data = request.json
    filename = data.get('filename', '')

    if not filename or not filename.endswith('.csv'):
        return jsonify({'error': 'Invalid filename'}), 400

    filepath = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'Uploaded file not found'}), 404

    try:
        os.remove(filepath)
        files = get_available_files()
        return jsonify({
            'message': f'File {filename} deleted successfully',
            'files': files
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """API endpoint to analyze weather data."""
    data = request.json
    filename = data.get('filename', '')
    
    if not filename or not filename.endswith('.csv'):
        return jsonify({'error': 'Invalid filename'}), 400
    
    upload_path = os.path.join(UPLOAD_DIR, filename)
    sample_path = os.path.join(DATA_DIR, filename)
    if os.path.exists(upload_path):
        filepath = upload_path
    elif os.path.exists(sample_path):
        filepath = sample_path
    else:
        return jsonify({'error': 'File not found'}), 404
    
    try:
        weather_data = load_data_from_csv(filepath)
        
        if not weather_data:
            return jsonify({'error': 'File is empty or invalid'}), 400
        
        return jsonify(build_response(filename, weather_data))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
