import requests
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = "8d6aa64634f067fa9a67a23bdade9ca7"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_weather_today(city_name):
    try:
        # Current weather data
        current_weather_url = f"{BASE_URL}weather?q={city_name}&appid={API_KEY}&units=metric"
        current_response = requests.get(current_weather_url)
        current_data = current_response.json()

        if current_response.status_code != 200:
            print(f"Error: {current_data.get('message', 'Unable to fetch data')}")
            return

        # Air quality data
        lat = current_data['coord']['lat']
        lon = current_data['coord']['lon']
        air_quality_url = f"{BASE_URL}air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        air_quality_response = requests.get(air_quality_url)
        air_quality_data = air_quality_response.json()

        # Current weather details
        print(f"Current Weather in {city_name}:")
        print(f"Temperature: {current_data['main']['temp']}°C")
        print(f"Min Temperature: {current_data['main']['temp_min']}°C")
        print(f"Max Temperature: {current_data['main']['temp_max']}°C")
        print(f"Feels Like: {current_data['main']['feels_like']}°C")
        print(f"Pressure: {current_data['main']['pressure']} hPa")
        print(f"Humidity: {current_data['main']['humidity']}%")
        print(f"Weather: {current_data['weather'][0]['description']}")
        print(f"Cloudiness: {current_data['clouds']['all']}%")
        print(f"Air Quality Index (AQI): {air_quality_data['list'][0]['main']['aqi']}")
        print()

    except Exception as e:
        print(f"An error occurred: {e}")

def get_weather_by_date(city_name, date):
    try:
        # Forecast data
        forecast_url = f"{BASE_URL}forecast?q={city_name}&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        if forecast_response.status_code != 200:
            print(f"Error: {forecast_data.get('message', 'Unable to fetch data')}")
            return

        # Find weather for the specified date
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        for entry in forecast_data['list']:
            entry_date = datetime.fromtimestamp(entry['dt']).date()
            if entry_date == target_date:
                print(f"Weather on {date} in {city_name}:")
                print(f"Temperature: {entry['main']['temp']}°C")
                print(f"Min Temperature: {entry['main']['temp_min']}°C")
                print(f"Max Temperature: {entry['main']['temp_max']}°C")
                print(f"Humidity: {entry['main']['humidity']}%")
                print(f"Weather: {entry['weather'][0]['description']}")
                print(f"Rain Probability: {entry.get('pop', 0) * 100}%")
                return

        print(f"No weather data available for {date} in {city_name}.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    while True:
        print("Weather App Menu:")
        print("1. Today's Weather for a City")
        print("2. Weather for a Specific Date")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter the city name: ")
            get_weather_today(city)
        elif choice == "2":
            city = input("Enter the city name: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            get_weather_by_date(city, date)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()