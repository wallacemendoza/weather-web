# `WEATHER_DASHBOARD`

```ascii
██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗     ██████╗  █████╗ ███████╗██╗  ██╗
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔════╝██║  ██║
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝    ██║  ██║███████║███████╗███████║
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ██║  ██║██╔══██║╚════██║██╔══██║
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║    ██████╔╝██║  ██║███████║██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

<div align="center">

### 🌦️ REAL-TIME WEATHER DASHBOARD WITH FLASK & PYTHON 🌦️

**`PYTHON`** × **`FLASK`** × **`WTTR.IN_API`** × **`RESPONSIVE_UI`**

*Clean, production-ready weather app with live conditions and 3-day forecasts for any city worldwide*

---

![Python](https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/FLASK-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-87.7%25-E34F26?style=for-the-badge&logo=html5&logoColor=white)

**Live Demo:** [weather-web-1-566j.onrender.com](https://weather-web-1-566j.onrender.com/)

</div>

---

## 🎯 `PROJECT_OVERVIEW`

**Full-stack weather dashboard** providing real-time meteorological data for any city in the world. Built with Python Flask backend and responsive HTML/CSS frontend, leveraging the wttr.in API for weather data without requiring API keys or authentication.

### `CORE_CAPABILITIES`

```yaml
framework: "Flask (Python web framework)"
data_source: "wttr.in API (no key required)"
deployment: "Render cloud platform"
features:
  - Real-time current conditions
  - 3-day weather forecast
  - Global city search
  - Quick-access city buttons
  - Color-coded temperature display
  - Responsive dark theme UI
```

---

## 🔥 `FEATURES_IMPLEMENTED`

<table>
<tr>
<td width="50%">

### `CURRENT_CONDITIONS`
```python
✓ Temperature (°F)
✓ "Feels like" temperature
✓ Wind speed & direction
✓ Humidity percentage
✓ UV index
✓ Atmospheric pressure
✓ Visibility distance
✓ Weather condition icon
```

</td>
<td width="50%">

### `FORECAST_DATA`
```python
✓ 3-day forecast
✓ High/Low temperatures
✓ Sunrise/sunset times
✓ Moon phase
✓ Weather descriptions
✓ Color-coded temps
✓ Quick city shortcuts
✓ Global city search
```

</td>
</tr>
</table>

### `TECHNICAL_IMPLEMENTATIONS`

| Feature | Technology | Purpose |
|---------|-----------|---------|
| **Backend Framework** | Flask (Python) | HTTP routing, API integration |
| **Weather Data** | wttr.in API | Real-time conditions & forecasts |
| **HTTP Client** | Requests library | API calls to wttr.in |
| **Template Engine** | Jinja2 (Flask default) | Dynamic HTML rendering |
| **Frontend** | HTML5, CSS3, JavaScript | Responsive UI components |
| **Deployment** | Render | Cloud hosting platform |
| **Process Manager** | Procfile | Production server config |

---

## 🛠️ `ARCHITECTURE`

```
╔═══════════════════════════════════════════════════════════════╗
║                     BROWSER (CLIENT)                           ║
║   • Search form (city input)                                  ║
║   • Display current conditions                               ║
║   • Show 3-day forecast                                      ║
║   • Quick city buttons (6 presets)                           ║
╚══════════════════════╦════════════════════════════════════════╝
                       ║ HTTP GET/POST
╔══════════════════════╩════════════════════════════════════════╗
║                   FLASK APPLICATION                            ║
║   Route: /                                                     ║
║   └─→ Render index.html template                             ║
║   Route: /weather (POST)                                      ║
║   └─→ Process city search                                     ║
║       └─→ Call wttr.in API                                    ║
║           └─→ Parse JSON response                             ║
║               └─→ Return data to template                     ║
╚══════════════════════╦════════════════════════════════════════╝
                       ║ HTTP GET (JSON)
╔══════════════════════╩════════════════════════════════════════╗
║                   WTTR.IN API SERVICE                          ║
║   Endpoint: https://wttr.in/{city}?format=j1                 ║
║   Returns: JSON with weather data                             ║
║   • Current conditions                                        ║
║   • 3-day forecast                                            ║
║   • Astronomy data (sunrise, sunset, moon)                   ║
╚═══════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT FLOW                           │
│                                                              │
│  Local Dev → Git Push → Render → Production Server          │
│  (port 5000)          (GitHub)   (Cloud)   (Live URL)       │
└─────────────────────────────────────────────────────────────┘
```

---

## 💾 `CODE_STRUCTURE`

### Flask Application (`app.py`)

```python
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    """Render main weather dashboard"""
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    """Fetch weather data for searched city"""
    city = request.form.get('city')
    
    # Call wttr.in API
    url = f'https://wttr.in/{city}?format=j1'
    response = requests.get(url)
    weather_data = response.json()
    
    # Extract current conditions
    current = weather_data['current_condition'][0]
    forecast = weather_data['weather'][:3]  # 3-day forecast
    
    # Parse and structure data
    data = {
        'city': city,
        'temp_f': current['temp_F'],
        'feels_like': current['FeelsLikeF'],
        'condition': current['weatherDesc'][0]['value'],
        'humidity': current['humidity'],
        'wind_speed': current['windspeedMiles'],
        'uv_index': current['uvIndex'],
        'pressure': current['pressure'],
        'visibility': current['visibilityMiles'],
        'forecast': format_forecast(forecast)
    }
    
    return render_template('index.html', weather=data)

def format_forecast(forecast_data):
    """Format forecast data for display"""
    formatted = []
    for day in forecast_data:
        formatted.append({
            'date': day['date'],
            'high': day['maxtempF'],
            'low': day['mintempF'],
            'sunrise': day['astronomy'][0]['sunrise'],
            'sunset': day['astronomy'][0]['sunset'],
            'moon_phase': day['astronomy'][0]['moon_phase']
        })
    return formatted

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 🎨 `USER_INTERFACE`

### Temperature Color Coding

```python
# Temperature ranges mapped to visual colors
def get_temp_color(temp_f):
    if temp_f >= 90:   return "#ff4444"  # Hot (red)
    elif temp_f >= 70: return "#ffa500"  # Warm (orange)
    elif temp_f >= 50: return "#ffeb3b"  # Mild (yellow)
    elif temp_f >= 32: return "#4fc3f7"  # Cool (light blue)
    else:              return "#2196f3"  # Cold (blue)
```

### Quick City Buttons

Pre-configured cities for instant weather lookup:
- 🇬🇧 London
- 🇯🇵 Tokyo
- 🇧🇷 Rio de Janeiro
- 🇺🇸 Atlanta
- 🇪🇸 Madrid
- 🇦🇺 Sydney

### Dark Theme UI
```css
/* Modern dark theme with good contrast */
background: #1a1a2e
primary-text: #ffffff
secondary-text: #a0a0a0
accent-color: #4fc3f7
card-background: #16213e
```

---

## ⚙️ `INSTALLATION_&_SETUP`

### Prerequisites

```bash
# Python 3.x required
python --version

# Pip package manager
pip --version
```

### Local Development

```bash
# Clone repository
git clone https://github.com/wallacemendoza/weather-web.git
cd weather-web

# Install dependencies
pip install -r requirements.txt

# Run Flask development server
python app.py

# Access application
# Open browser to http://localhost:5000
```

### Dependencies (`requirements.txt`)

```
Flask==3.0.0
requests==2.31.0
gunicorn==21.2.0
```

---

## 🚀 `DEPLOYMENT`

### Render Deployment

**Procfile** configuration:
```
web: gunicorn app:app
```


**Live URL:** https://weather-web-1-566j.onrender.com/

---

## 🎯 `USAGE_WORKFLOWS`

### Search Any City

```
1. User enters city name (e.g., "New York")
2. Clicks "Search" button or presses Enter
3. Flask processes POST request
4. Backend calls wttr.in API
5. JSON response parsed
6. Data rendered in template
7. User sees:
   - Current conditions (temp, wind, humidity, etc.)
   - 3-day forecast (highs/lows, astronomy)
   - Color-coded temperature display
```

### Quick City Selection

```
1. User clicks pre-configured city button
2. JavaScript auto-fills search form
3. Form submits automatically
4. Weather data loads for selected city
```

---

## 📊 `API_INTEGRATION`

### wttr.in API Endpoint

```bash
# Request format
GET https://wttr.in/{city}?format=j1

# Example
GET https://wttr.in/London?format=j1

# Response (JSON)
{
  "current_condition": [
    {
      "temp_F": "72",
      "FeelsLikeF": "68",
      "weatherDesc": [{"value": "Partly cloudy"}],
      "humidity": "65",
      "windspeedMiles": "10",
      "uvIndex": "4",
      "pressure": "1013",
      "visibilityMiles": "10"
    }
  ],
  "weather": [
    {
      "date": "2026-02-18",
      "maxtempF": "75",
      "mintempF": "62",
      "astronomy": [
        {
          "sunrise": "06:30 AM",
          "sunset": "05:45 PM",
          "moon_phase": "Waxing Crescent"
        }
      ]
    }
    // ... 2 more days
  ]
}
```

**Key Advantages:**
- ✅ No API key required
- ✅ No rate limits for reasonable use
- ✅ Global city coverage
- ✅ Comprehensive data (current + forecast)
- ✅ JSON format (easy parsing)

---

## 📁 `PROJECT_STRUCTURE`

```
weather-web/
├── app.py                    # Flask application (backend)
├── requirements.txt          # Python dependencies
├── Procfile                  # Render deployment config
├── gitignore                 # Git ignore patterns
├── README.md                 # Project documentation
└── templates/
    └── index.html            # Frontend template (UI)

Lines of Code:
- app.py: ~100 lines (Python/Flask)
- index.html: ~300 lines (HTML/CSS/JS)
Total: ~400 lines
```

---

## 🔬 `TECHNICAL_HIGHLIGHTS`

Demonstrates proficiency in:

- **Flask Framework**: Routing, templates, HTTP methods
- **REST API Integration**: External API consumption
- **HTTP Requests**: GET/POST handling
- **JSON Parsing**: Data extraction and formatting
- **Template Rendering**: Dynamic HTML with Jinja2
- **Responsive Design**: Mobile-friendly UI
- **Cloud Deployment**: Production hosting on Render
- **Python Best Practices**: Clean code, error handling
- **Full-Stack Development**: Backend + Frontend integration

**Real-World Application**: Weather apps are fundamental web applications demonstrating API integration and user interface design.

---

## 🧪 `TESTING`

### Manual Testing Checklist

```
✓ Search functionality (valid city names)
✓ Error handling (invalid cities)
✓ Quick city buttons work
✓ Temperature color coding accurate
✓ Forecast displays correctly
✓ Mobile responsiveness
✓ API timeout handling
✓ Page load performance
```

### Example Test Cases

```python
# Test city search
assert search_weather("London") returns valid data
assert search_weather("XYZ123") handles gracefully

# Test temperature conversion
assert parse_temp("72°F") displays with correct color
assert parse_temp("32°F") shows as blue (cold)

# Test forecast parsing
assert get_forecast() returns 3 days of data
assert forecast includes sunrise/sunset times
```

---

## 🌟 `FEATURES_ROADMAP`

**Future Enhancements:**
- [ ] 7-day forecast option
- [ ] Hourly forecast data
- [ ] Weather alerts/warnings
- [ ] Geolocation auto-detect
- [ ] Celsius/Fahrenheit toggle
- [ ] Save favorite cities
- [ ] Historical weather data
- [ ] Weather maps integration
- [ ] Social sharing
- [ ] PWA (offline support)

---

## 🐛 `TROUBLESHOOTING`

### Common Issues

**API Not Responding:**
```python
# Check internet connection
# wttr.in may be temporarily down
# Add timeout to requests:
requests.get(url, timeout=10)
```

**City Not Found:**
```python
# Ensure correct spelling
# Try variations (e.g., "NYC" vs "New York City")
# Some cities require state/country (e.g., "Paris, France")
```

**Port Already in Use:**
```bash
# Change port in app.py:
app.run(port=5001)
```

---

## 📜 `LICENSE_&_USAGE`

```
┌─────────────────────────────────────────────────────────┐
│  WEATHER DASHBOARD DEMONSTRATION                         │
│                                                          │
│  Flask-based weather application showcasing API          │
│  integration and full-stack development patterns.        │
│  Portfolio demonstration of web development skills.      │
│                                                          │
│  ⚠️  Personal/portfolio project                      │
│  ⚠️  Not for commercial deployment                     │
│  ✓  Available for technical review                      │
│  ✓  Open to discussion                                  │
└─────────────────────────────────────────────────────────┘
```

**Third-Party Services:**
- wttr.in API (free service, no authentication)
- Render (cloud hosting platform)

---

## 🚀 `AUTHOR`

**Wallace Mendoza** — *Full-Stack Developer*

Specializing in Python web applications, API integration, and responsive UI design.

[GitHub](https://github.com/wallacemendoza) • [Portfolio](https://wallacemendoza.github.io/portfolio/)

---

<div align="center">

### `TECH_FINGERPRINT`

`PYTHON` • `FLASK` • `REST_API` • `HTML` • `CSS` • `RESPONSIVE_UI` • `CLOUD_DEPLOY`

---

*Simple. Fast. Beautiful weather data.*

**[⬆ back to top](#weather_dashboard)**

</div>
