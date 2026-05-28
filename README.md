# 🌤️ Weather Project

A Python weather data analysis project that processes CSV files and generates comprehensive weather summaries.

## Features

- ✅ Load weather data from CSV files
- ✅ Calculate temperature statistics (min, max, averages)
- ✅ Convert temperatures from Fahrenheit to Celsius
- ✅ Format dates in a human-readable format
- ✅ Generate overall and daily weather summaries
- ✅ **Beautiful web interface for data visualization**
- ✅ Comprehensive unit tests for all functions

## Project Structure

```
.
├── weather.py              # Core weather functions
├── main.py                 # CLI interface for weather analysis
├── app.py                  # Flask web application ⭐ NEW
├── tests/                  # Unit tests
│   ├── test_*.py          # Individual test files
│   ├── data/              # Sample CSV weather data
│   └── expected_output/   # Expected test outputs
├── templates/             # HTML templates ⭐ NEW
│   └── index.html         # Main web page
└── README.md
```

## Installation

1. Make sure you have Python 3.7+ installed
2. Navigate to the project directory

3. Install Flask (required for web interface):
   ```bash
   pip install flask
   ```

## 🚀 Running the Project

### Option 1: Web Interface (Recommended for Presentations) ⭐

Beautiful, interactive web interface:

```bash
python app.py
```

Then open: `http://localhost:5000`

**Features:**
- 🎨 Beautiful gradient UI with smooth animations
- 📱 Responsive design (works on mobile too)
- 📊 Select and analyze files with one click
- 📈 View data organized in clear sections
- ⚡ Real-time processing feedback

### Option 2: Command Line Interface

Interactive menu-based CLI:

```bash
python main.py
```

### Option 3: Run Tests

Verify all functions work correctly:

```bash
python -m unittest tests/*.py
```

## Core Functions in `weather.py`

### Temperature & Formatting
- `convert_f_to_c()` - Fahrenheit to Celsius conversion
- `format_temperature()` - Formats temperature with °C symbol

### Data Processing
- `load_data_from_csv()` - Reads CSV weather data
- `calculate_mean()` - Computes average temperature

### Date Handling
- `convert_date()` - Converts ISO format to readable date (e.g., "Friday 02 July 2021")

### Statistics
- `find_min()` - Finds minimum temperature and its position
- `find_max()` - Finds maximum temperature and its position

### Summaries
- `generate_summary()` - Overall weather summary (min, max, averages)
- `generate_daily_summary()` - Per-day weather breakdown

## Sample Data

3 example CSV files included in `tests/data/`:
- `example_one.csv` - 5 days (July 2021)
- `example_two.csv` - 8 days (June 2020)  
- `example_three.csv` - 8 days (Mixed values)

## Example Output

### General Summary
```
5 Day Overview
  The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
  The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
  The average low this week is 12.2°C.
  The average high this week is 17.8°C.
```

### Daily Summary
```
---- Friday 02 July 2021 ----
  Minimum Temperature: 9.4°C
  Maximum Temperature: 19.4°C

---- Saturday 03 July 2021 ----
  Minimum Temperature: 13.9°C
  Maximum Temperature: 20.0°C
```

## Testing

```bash
# Run all tests
python -m unittest tests -v

# Run specific test
python -m unittest tests/test_convert_f_to_c.py

# Test a single function
python -m unittest tests.test_calculate_mean.CalculateMeanTests.test_calculate_mean
```

## Tech Stack

- 🐍 Python 3.7+
- 🌐 Flask (web framework)
- 📊 CSV (data format)
- ✅ unittest (testing)

## For Presentations

1. **Impressive Demo:** `python app.py` → Open browser → Select file → ✨
2. **Show Tests:** `python -m unittest tests -v` → All green ✅
3. **Interactive CLI:** `python main.py` → Explain step-by-step