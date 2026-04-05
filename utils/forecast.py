def get_forecast_summary(weather_data):
    """
    Generates a simple forecast-style summary based on current weather.
    """
    if "error" in weather_data:
        return "Forecast unavailable."

    condition = weather_data["condition"].lower()
    temp = weather_data["temperature"]

    if "rain" in condition:
        return "🌧️ Rain is expected. Carry an umbrella."
    elif "cloud" in condition:
        return "☁️ Cloudy conditions expected."
    elif temp > 35:
        return "🔥 Very hot weather. Stay hydrated."
    elif temp < 15:
        return "🥶 Cool weather. Consider warm clothing."
    else:
        return "🌤️ Weather looks fairly stable today."
