import streamlit as st
from utils.weather_fetcher import get_weather
from utils.forecast import get_forecast_summary
from utils.weather_summary import build_weather_summary

st.set_page_config(page_title="Weather Agent", page_icon="🌦️", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main-title {
            font-size: 3rem;
            font-weight: 800;
            color: white;
        }
        .hero-box {
            background: linear-gradient(90deg, #0f2027, #2c5364);
            padding: 2rem;
            border-radius: 25px;
            color: white;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.12);
        }
        .feature-card {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
            border: 1px solid #e8edf5;
            min-height: 220px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="hero-box">
    <div class="main-title">🌦️ Weather Agent</div>
    <p style="font-size: 1.2rem; margin-top: 1rem;">
        A smart weather assistant that provides real-time forecasts,
        temperature updates, climate insights, and location-based weather information.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# --- Features ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h2>🌍 Location-Based Search</h2>
        <p>Check live weather conditions for any city or location.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h2>🌡️ Real-Time Weather</h2>
        <p>Get temperature, humidity, wind speed, and current conditions instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h2>☁️ Forecast Insights</h2>
        <p>Receive quick summaries and weather outlook suggestions.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# --- Input ---
st.subheader("📍 Enter Location")
city = st.text_input(
    "Enter city name:",
    placeholder="Example: Hyderabad, London, New York..."
)

if st.button("Get Weather"):
    if city.strip():
        weather_data = get_weather(city)

        if "error" in weather_data:
            st.error(weather_data["error"])
        else:
            summary = build_weather_summary(weather_data)
            forecast = get_forecast_summary(weather_data)

            st.subheader("📋 Weather Report")
            st.info(summary)

            st.subheader("🌤️ Forecast Summary")
            st.success(forecast)
    else:
        st.error("Please enter a city name.")
