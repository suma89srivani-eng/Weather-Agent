def build_weather_summary(weather_data):
    """
    Creates a readable weather summary for the UI.
    """
    if "error" in weather_data:
        return weather_data["error"]

    return (
        f"Current weather in {weather_data['city']}, {weather_data['country']}:\n"
        f"- Temperature: {weather_data['temperature']}°C\n"
        f"- Feels Like: {weather_data['feels_like']}°C\n"
        f"- Condition: {weather_data['condition']} ({weather_data['description']})\n"
        f"- Humidity: {weather_data['humidity']}%\n"
        f"- Wind Speed: {weather_data['wind_speed']} m/s"
    )
