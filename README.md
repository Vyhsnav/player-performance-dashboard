# ⚽ Player Performance Dashboard

A web application that lets you search, explore, and compare football (soccer) player statistics using live data from the [football-data.org](https://www.football-data.org/) API.

Built as a portfolio project to practice full-stack development, REST API integration, and data visualization.

---

## 🚀 Features

### ✅ Core Features
- **Player Search** — Search any player by name and view their profile
- **Season Stats Cards** — At-a-glance display of goals, assists, appearances, and minutes played
- **Performance Charts** — Visual bar/line charts of a player's stats across recent matches
- **Team Info & Standings** — Browse team squads and current league standings

### ⚖️ Player Comparison
- Search two players simultaneously and compare their stats side by side
- Dual-dataset Chart.js visualization to contrast performance visually

### 🟡 Stretch Goals (Planned)
- Match Results Feed — Recent results for any selected team
- Favorites / Bookmarking — Save frequently searched players using localStorage

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python + Flask |
| Visualization | Chart.js |
| Data Source | football-data.org API |
| Deployment | Render / Railway |

---

## 📁 Project Structure

```
player-performance-dashboard/
│
├── backend/
│   ├── app.py          # Flask server and API routes
│   └── fetch.py        # football-data.org API calls
│
├── frontend/
│   ├── index.html      # Main search and dashboard page
│   ├── pages/          # Additional HTML pages
│   ├── css/
│   │   └── style.css   # Styling
│   └── js/
│       └── main.js     # Fetch calls and DOM manipulation
│
├── data/               # Any cached or sample JSON data
├── .env.example        # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/player-performance-dashboard.git
cd player-performance-dashboard
```

### 2. Set up the backend
```bash
cd backend
pip install -r ../requirements.txt
```

### 3. Add your API key
```bash
cp .env.example .env
# Edit .env and add your football-data.org API key
```

Get a free API key at [football-data.org](https://www.football-data.org/client/register)

### 4. Run the Flask server
```bash
python app.py
```

### 5. Open the frontend
Open `frontend/index.html` in your browser or serve it with Live Server (VS Code extension).

---

## 📸 Screenshots

*Coming soon as the project develops.*

---

## 🗺️ Milestones

| Week | Goal |
|---|---|
| Week 1 | Setup, API key, fetch raw data in terminal |
| Week 2 | Flask backend with working endpoints |
| Week 3 | Frontend connected, stats displaying |
| Week 4 | Charts, comparison feature, polish & deploy |

---

## 📚 What I'm Learning

- REST API consumption and JSON parsing
- Client-server architecture with Flask
- Data visualization with Chart.js
- Git and project structuring
- Basic deployment on cloud platforms

---

## 🙋 Author

**Vyshnav** — B.Tech CS student at Model Engineering College, Ernakulam  
[GitHub](https://github.com/YOUR_USERNAME) • [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

---

## 📄 License

MIT License
