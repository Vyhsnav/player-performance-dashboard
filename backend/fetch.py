import requests

API_KEY = "dfcc31e8d468455eaf1181899e8ce993"
BASE_URL = "https://api.football-data.org/v4"

headers = {"X-Auth-Token": API_KEY}

def get_standings(competition="PL"):
    url = f"{BASE_URL}/competitions/{competition}/standings"
    response = requests.get(url, headers=headers)
    data = response.json()
    
    standings = data["standings"][0]["table"]
    
    print("🏆 Premier League Standings\n")
    for team in standings[:10]:
        print(f"{team['position']}. {team['team']['name']} — {team['points']} pts | W:{team['won']} D:{team['draw']} L:{team['lost']}")


def get_team(team_id):
    url = f"{BASE_URL}/teams/{team_id}"
    response = requests.get(url , headers=headers)
    data = response.json()

    print(f"\n📋 {data['name']}")
    print(f"Stadium: {data['venue']}")
    print(f"Founded: {data['founded']}")
    print(f"\nSquad:")
    for player in data['squad']:
        print(f" - {player['name']} ({player['position']})")

def get_player(player_id):
    url=f"{BASE_URL}/persons/{player_id}"
    response = requests.get(url , headers=headers)
    data = response.json()

    print(f"\n👤 {data['name']}")
    print(f"NAtionality: {data['nationality']}")
    print(f"Position: {data['position']}")
    print(f"Date of Birth: {data['dateOfBirth']}")

    if 'currentTeam' in data and data['currentTeam']:
        print(f"Current Team: {data['currentTeam']['name']}")


