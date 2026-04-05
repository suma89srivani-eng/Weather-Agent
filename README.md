# 🌦️ Weather Agent

Weather Agent is a smart AI-based weather assistant that helps users access real-time weather conditions, forecast updates, temperature details, and location-based climate insights through an interactive interface.

## 🚀 Features

- 🌍 Location-based weather search
- 🌡️ Real-time temperature and weather conditions
- ☁️ Forecast updates
- 💨 Humidity, wind speed, and climate details
- 🎨 Clean and user-friendly UI

## 📸 Preview

![Weather Agent Home](assets/screenshot-home.png)

---

## 📂 Project Structure

```bash
weather-agent/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── LICENSE
│
├── data/
│   └── sample_locations.json
│
├── utils/
│   ├── __init__.py
│   ├── weather_fetcher.py
│   ├── forecast.py
│   ├── weather_summary.py
│   └── prompts.py
│
├── assets/
│   ├── screenshot-home.png
│   └── logo.png
│
└── .github/
    └── workflows/
        └── python-app.yml
