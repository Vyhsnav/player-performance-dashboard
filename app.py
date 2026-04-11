from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "dfcc31e8d468455eaf1181899e8ce993"
BASE_URL = "https://api.football-data.org/v4"
headers = {"X-Auth-Token": API_KEY}

@app.route("/api/standings")

def standings():
    url = f"{BASE_URL}/competitions/PL/standings"
    response = requests.get(url , headers=headers)
    data = response.json()

    table = data["standings"][0]["table"]
    result = []
    for team in table:
        result.append({
            "position": team['position'],
            "team": team['team']['name'],
            "points": team['points'],
            "won": team['won'],
            "draw": team['draw'],
            "lost": team['lost'],
            "crest": team['team']['crest'],
            "played": team['playedGames']
        })
    return jsonify(result)
    
@app.route("/api/team/<int:team_id>")

def team(team_id):
    url = f"{BASE_URL}/teams/{team_id}"
    response = requests.get(url , headers=headers)
    data = response.json()

    result = {
        "name": data['name'],
        "venue": data['venue'],
        "founded": data['founded'],
        "crest": data["crest"],

        "squad": [{"name": p['name'],"position": p['position']} for p in data['squad']]
    }
    return jsonify(result)

@app.route("/api/player/<int:player_id>")

def player(player_id):
    url = f"{BASE_URL}/persons/{player_id}"
    response = requests.get(url , headers=headers)
    data = response.json()

    result = {
        "name": data['name'],
        "nationality": data['nationality'],
        "position": data['position'],
        "dateOfBirth": data['dateOfBirth'],
        "currentTeam": data['currentTeam']['name'] if 'currentTeam' in data and data['currentTeam'] else None

    }
    return jsonify(result)

@app.route("/api/test")
def test():
    return jsonify({"status": "working"})

if __name__ == "__main__":
    app.run(debug=False, port=3001)