# 🌤️ Weather Project

A Python weather data analysis project that loads CSV files, converts temperatures to Celsius, and presents both a clean web interface and unit-tested backend logic.

## What’s included

- ✅ Web application built with Flask
- ✅ File upload and deletion support
- ✅ Built-in sample CSV data in `tests/data/`
- ✅ Summary and daily summary generation
- ✅ Full unit test coverage for weather utilities
- ✅ `uploaded_data/` folder for user uploads

## Project structure

```
.
├── app.py                  # Flask web application entry point
├── weather.py              # Core weather data processing functions
├── main.py                 # CLI interface for the project
├── requirements.txt        # Python dependencies
├── .python-version         # Python version for deployment environments
├── Procfile                # Heroku entry point
├── templates/              # HTML templates for Flask
│   └── index.html         # Main web UI
├── tests/                  # Unit tests and sample data
│   ├── data/              # Example CSV files
│   └── expected_output/   # Expected outputs for tests
└── uploaded_data/          # Uploaded CSV files stored locally
```

## Installation

1. Make sure you have Python 3.11 installed.
2. Open a terminal in the project folder.
3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the web app

The project is deployed and available at:

```text
https://weather-python-project-15ced61538aa.herokuapp.com/
```

To run it locally, start the Flask application:

```bash
python app.py
```

Open your browser at:

```text
http://localhost:5000
```

### What you can do in the UI

- Select one of the sample CSV files
- Upload your own CSV file
- View the generated overall summary
- View the daily summary
- Delete uploaded files

## Run the CLI

If you prefer terminal mode:

```bash
python main.py
```

## Run tests

Execute all unit tests with:

```bash
python -m unittest tests -v
```

## About the backend

The `weather.py` module contains the core analysis logic:

- `load_data_from_csv()` — loads CSV weather data
- `convert_f_to_c()` — converts Fahrenheit to Celsius
- `convert_date()` — formats ISO dates into readable text
- `find_min()` / `find_max()` — finds temperature extremes
- `generate_summary()` — builds overall summary text
- `generate_daily_summary()` — builds per-day summary text

## Sample data

Sample CSV files live in `tests/data/`:

- `example_one.csv`
- `example_two.csv`
- `example_three.csv`

Uploaded files are stored locally in `uploaded_data/` while the app runs.

## Deployment notes

- `requirements.txt` includes `Flask==3.0.0` and `gunicorn==21.2.0`
- `Procfile` is configured for Heroku: `web: gunicorn app:app`
- `.python-version` is set to `3.11`

## Notes

- Use `uploaded_data/` only for temporary local uploads.
- Sample files remain in `tests/data/` so the app can always analyze demo data.
- The web UI is the recommended way to show the project to others.
