class WeatherFetcher:
    def fetch_weather_data(self, city):
        # Convert the input city name to lowercase
        city = city.lower()
        
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"city": "New York", "temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"city": "London", "temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"city": "Tokyo", "temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city)



class WeatherParser:
    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        temperature = data.get("temperature")
        condition = data.get("condition")
        humidity = data.get("humidity")
        city = data.get("city")
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
