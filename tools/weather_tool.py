import os
import requests
from langchain_core.tools import tool

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
print(f'WEather API key : {WEATHER_API_KEY}')

@tool
def get_weather(city: str) -> str:
    """Fetches current weather information for a given city."""
    if not WEATHER_API_KEY:
        return "Weather API key is missing."

    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
        )

        if response.status_code != 200:
            return f"Could not fetch weather for '{city}'. Status code: {response.status_code}"

        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        return f"The weather in {city} is currently '{weather}' with a temperature of {temperature}°C."
    
    except Exception as e:
        return f"An error occurred while fetching weather: {str(e)}"
