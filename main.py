"""
Main script for running the Weather Project.
Loads a weather CSV file and prints two summaries:
1. A general summary (min, max, averages)
2. A daily summary (per day)
"""

import os
from weather import load_data_from_csv, generate_summary, generate_daily_summary


def get_csv_file():
    """Allows the user to select a CSV file from the sample data."""
    data_dir = "tests/data"
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    if not files:
        print("❌ No CSV files found in tests/data/")
        return None
    
    print("\n📊 Available weather data files:")
    for i, file in enumerate(files, 1):
        print(f"  {i}. {file}")
    
    while True:
        try:
            choice = input("\nChoose a file number (or q to quit): ").strip()
            if choice.lower() == 'q':
                return None
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                return os.path.join(data_dir, files[idx])
            print("❌ Invalid choice. Please try again.")
        except ValueError:
            print("❌ Enter a number or 'q'.")


def display_summary(filepath):
    """Loads data and prints both summaries."""
    try:
        print(f"\n📂 Loading data from: {filepath}")
        weather_data = load_data_from_csv(filepath)
        
        if not weather_data:
            print("⚠️  File is empty or invalid.")
            return
        
        print(f"✅ Loaded {len(weather_data)} days of data.\n")
        
        # General summary
        print("=" * 60)
        print("📈 GENERAL SUMMARY")
        print("=" * 60)
        summary = generate_summary(weather_data)
        print(summary)
        
        # Daily summary
        print("=" * 60)
        print("📅 DAILY SUMMARY")
        print("=" * 60)
        daily_summary = generate_daily_summary(weather_data)
        print(daily_summary)
        
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
    except Exception as e:
        print(f"❌ Error processing file: {e}")


def main():
    """Main entry point for the program."""
    print("\n" + "🌤️  WEATHER PROJECT - WEATHER DATA ANALYSIS".center(60))
    print("=" * 60)
    
    csv_file = get_csv_file()
    if csv_file:
        display_summary(csv_file)
        print("\n✅ Done!")
    else:
        print("\n👋 Goodbye!")


if __name__ == "__main__":
    main()
