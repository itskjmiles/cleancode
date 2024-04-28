from weather import WeatherFetcher, WeatherParser

def get_detailed_forecast(city):
    fetcher = WeatherFetcher()
    parser = WeatherParser()
    data = fetcher.fetch_weather_data(city)
    return parser.parse_weather_data(data)

def display_weather(city):
    fetcher = WeatherFetcher()
    parser = WeatherParser()
    data = fetcher.fetch_weather_data(city)
    if not data:
        return f"Weather data not available for {city}"
    else:
        return parser.parse_weather_data(data)

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = get_detailed_forecast(city)
        else:
            forecast = display_weather(city)
        print(forecast)


if __name__ == "__main__":
    main()