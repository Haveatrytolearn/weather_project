import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_obj = datetime.fromisoformat(iso_string)
    return date_obj.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(celsius, 1)
    


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    if not weather_data:
        return 0
    total = sum(float(temp) for temp in weather_data)
    return total / len(weather_data)
    


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.
    
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row if present
        for row in reader:
            if row:  # skip empty lines
                converted_row = [row[0], int(row[1]), int(row[2])]
                data.append(converted_row)
    return data



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    float_data = [float(temp) for temp in weather_data]
    min_value = min(float_data)
    
    # Find the last index of the minimum value
    min_index = len(float_data) - 1 - float_data[::-1].index(min_value)
    
    return (min_value, min_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
            return ()
    
    float_data = [float(temp) for temp in weather_data]
    max_value = max(float_data)
    
    # Find the last index of the maximum value
    max_index = len(float_data) - 1 - float_data[::-1].index(max_value)
    
    return (max_value, max_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return ""
    
    min_temps = [float(row[1]) for row in weather_data]
    max_temps = [float(row[2]) for row in weather_data]
    
    min_value, min_index = find_min(min_temps)
    max_value, max_index = find_max(max_temps)
    
    min_celsius = convert_f_to_c(min_value)
    max_celsius = convert_f_to_c(max_value)
    
    min_date = convert_date(weather_data[min_index][0])
    max_date = convert_date(weather_data[max_index][0])
    
    avg_min = calculate_mean(min_temps)
    avg_max = calculate_mean(max_temps)
    
    avg_min_celsius = convert_f_to_c(avg_min)
    avg_max_celsius = convert_f_to_c(avg_max)
    
    summary = f"{len(weather_data)} Day Overview\n"
    summary += f"  The lowest temperature will be {format_temperature(min_celsius)}, and will occur on {min_date}.\n"
    summary += f"  The highest temperature will be {format_temperature(max_celsius)}, and will occur on {max_date}.\n"
    summary += f"  The average low this week is {format_temperature(avg_min_celsius)}.\n"
    summary += f"  The average high this week is {format_temperature(avg_max_celsius)}.\n"
    
    return summary




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return ""
    
    summary = ""
    
    for day in weather_data:
        if len(day) >= 3:
            date_str = convert_date(day[0])
            min_temp_c = convert_f_to_c(day[1])
            max_temp_c = convert_f_to_c(day[2])
            min_temp_formatted = format_temperature(min_temp_c)
            max_temp_formatted = format_temperature(max_temp_c)
            summary += f"---- {date_str} ----\n"
            summary += f"  Minimum Temperature: {min_temp_formatted}\n"
            summary += f"  Maximum Temperature: {max_temp_formatted}\n"
            summary += "\n"
    
    return summary