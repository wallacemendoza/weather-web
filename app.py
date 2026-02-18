"""
app.py — Flask Weather Web App
A live weather dashboard accessible from any browser.
"""

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def fetch_weather(city: str) -> dict | None:
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # wttr.in returns a weird response for unknown cities
        if not data.get("current_condition"):
            return None
        return data
    except Exception:
        return None

def parse_weather(data: dict, city: str) -> dict:
    current = data["current_condition"][0]
    nearest = data["nearest_area"][0]
    area = nearest["areaName"][0]["value"]
    country = nearest["country"][0]["value"]

    forecast = []
    for i, day in enumerate(data["weather"][:3]):
        hourly = day["hourly"]
        mid = hourly[len(hourly) // 2]
        forecast.append({
            "date": day["date"],
            "label": ["Today", "Tomorrow", "Day After"][i],
            "max_c": day["maxtempC"],
            "min_c": day["mintempC"],
            "desc": mid["weatherDesc"][0]["value"],
            "sunrise": day["astronomy"][0]["sunrise"],
            "sunset": day["astronomy"][0]["sunset"],
            "moon": day["astronomy"][0]["moon_phase"],
        })

    return {
        "city": city.title(),
        "area": area,
        "country": country,
        "temp_c": current["temp_C"],
        "feels_c": current["FeelsLikeC"],
        "humidity": current["humidity"],
        "desc": current["weatherDesc"][0]["value"],
        "wind_kmph": current["windspeedKmph"],
        "wind_dir": current["winddir16Point"],
        "visibility": current["visibility"],
        "uv": current["uvIndex"],
        "pressure": current["pressure"],
        "forecast": forecast,
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()
    if not city:
        return jsonify({"error": "Please enter a city name."}), 400

    data = fetch_weather(city)
    if not data:
        return jsonify({"error": f"Could not find weather for '{city}'. Try another city."}), 404

    return jsonify(parse_weather(data, city))

if __name__ == "__main__":
    app.run(debug=True)