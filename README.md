# 🌦️ weather-web

> A live weather dashboard you can open in any browser — built with Python & Flask.

Search any city and get real-time weather conditions plus a 3-day forecast, all in a beautiful dark UI.

---

## ✨ Features

- 🔍 **Search any city** — type and press Enter or click Search
- 🌡️ **Live current conditions** — temperature, humidity, wind, UV, pressure, visibility
- 📅 **3-day forecast** — high/low, sunrise/sunset, moon phase
- 🎨 **Color-coded temperatures** — from icy blue to blazing red
- ⚡ **Quick city buttons** — London, Tokyo, Rio, Atlanta, Madrid, Sydney
- 🔑 **No API key needed** — uses the free wttr.in service

---

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/weather-web.git
cd weather-web
pip install -r requirements.txt
python app.py
```

Then open your browser and go to: **http://localhost:5000**

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web server & routing |
| `requests` | Fetch weather from wttr.in |

---

## 📁 Project Structure

```
weather-web/
├── app.py                  # Flask backend
├── requirements.txt        # Dependencies
├── README.md
└── templates/
    └── index.html          # Frontend UI
```

---

## 📄 License

MIT License

---

<p align="center">Built with Python, Flask & ☕</p>
