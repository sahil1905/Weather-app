import requests
from datetime import datetime, timedelta

# Replace 'YOUR_API_KEY' with your actual API key from weatherapi.com
api_key = '9bad72b686cd44f1aec63112240601'

def get_weather(city, units='metric'):
    base_url = f'http://api.weatherapi.com/v1/forecast.json?key=e6551b9fb5294625812164803230910&q=London&days=1&aqi=yes&alerts=yes'

    response = requests.get(base_url)

    if response.status_code == 200:
        weather_data = response.json()
        current = weather_data['current']
        temperature = current['temp_c'] if units == 'metric' else current['temp_f']
        description = current['condition']['text']
        humidity = current['humidity']
        wind_speed = current['wind_kph']

        print(f"Weather in {city} ({units}):")
        print(f"Temperature: {temperature}°C" if units == 'metric' else f"Temperature: {temperature}°F")
        print(f"Description: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
    else:
        print(f"Error fetching weather data for {city}. Please check the city name.")

def get_weather_for_future_date(city, units='metric', days_in_future=1):
    future_date = datetime.now() + timedelta(days=days_in_future)
    formatted_date = future_date.strftime('%Y-%m-%d')

    base_url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days_in_future}&aqi=no&dt={formatted_date}'

    response = requests.get(base_url)

    if response.status_code == 200:
        weather_data = response.json()
        forecast_day = weather_data['forecast']['forecastday'][0]
        date = forecast_day['date']
        max_temp = forecast_day['day']['maxtemp_c'] if units == 'metric' else forecast_day['day']['maxtemp_f']
        min_temp = forecast_day['day']['mintemp_c'] if units == 'metric' else forecast_day['day']['mintemp_f']
        description = forecast_day['day']['condition']['text']

        print(f"Weather in {city} ({units}) on {date}:")
        print(f"Max Temperature: {max_temp}°C" if units == 'metric' else f"Max Temperature: {max_temp}°F")
        print(f"Min Temperature: {min_temp}°C" if units == 'metric' else f"Min Temperature: {min_temp}°F")
        print(f"Description: {description.capitalize()}")
    else:
        print(f"Error fetching weather data for {city}. Please check the city name.")

if __name__ == "__main__":
    print("Welcome to the Weather App!")

    while True:
        print("\nChoose an option:")
        print("1. Current Weather (Metric)")
        print("2. Current Weather (Imperial)")
        print("3. Weather for Tomorrow")
        print("4. Weather for the Day After Tomorrow")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            city = input("Enter city name: ")
            get_weather(city, units='metric')
        elif choice == '2':
            city = input("Enter city name: ")
            get_weather(city, units='imperial')
        elif choice == '3':
            city = input("Enter city name: ")
            get_weather_for_future_date(city, units='metric', days_in_future=1)
        elif choice == '4':
            city = input("Enter city name: ")
            get_weather_for_future_date(city, units='metric', days_in_future=2)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            