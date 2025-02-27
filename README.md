# Weather App

A simple command-line weather application that fetches current and future weather forecasts using the WeatherAPI service.

## Features
- Get the current weather in metric (Celsius) or imperial (Fahrenheit) units.
- Fetch weather forecasts for tomorrow or the day after tomorrow.
- Provides temperature, humidity, wind speed, and a brief weather description.

## Prerequisites
- Python 3.x installed on your system.
- An API key from [WeatherAPI](https://www.weatherapi.com/) (Replace `YOUR_API_KEY` in the code).
- `requests` module installed.

## Installation
1. Clone this repository or download the script.
2. Install required dependencies using pip:
   ```sh
   pip install requests
   ```
3. Replace `YOUR_API_KEY` in the script with your actual WeatherAPI key.

## Usage
Run the script using Python:
```sh
python weather_app.py
```

### Menu Options
1. **Current Weather (Metric)** - Enter the city name to get the current weather in Celsius.
2. **Current Weather (Imperial)** - Enter the city name to get the current weather in Fahrenheit.
3. **Weather for Tomorrow** - Enter the city name to get the forecast for the next day.
4. **Weather for the Day After Tomorrow** - Enter the city name to get the forecast two days ahead.
5. **Exit** - Quit the application.

## Example Output
```
Welcome to the Weather App!

Choose an option:
1. Current Weather (Metric)
2. Current Weather (Imperial)
3. Weather for Tomorrow
4. Weather for the Day After Tomorrow
5. Exit
Enter your choice (1/2/3/4/5): 1
Enter city name: London
Weather in London (metric):
Temperature: 15°C
Description: Partly cloudy
Humidity: 78%
Wind Speed: 12 km/h
```

## Known Issues
- Ensure the API key is valid and has sufficient requests available.
- Check for typos in city names as incorrect names might not return results.

## Author
Developed by Sahil Parikh.

