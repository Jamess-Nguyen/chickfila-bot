import sys
import requests
import json


def fetch_runs(game_id):
    """

    Accepts a specific mlb game ID and curls the game data
    You can review example data at:
    https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary?event=401570673

    """

    url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary?event={game_id}"
    response = requests.get(url)
    game_dict = json.loads(response.content)
    
    for team in game_dict["boxscore"]["teams"]:
        if team["team"]["abbreviation"]!="LAA":
            continue
        if team["team"]["abbreviation"]=="LAA":
            for stats in team["statistics"][0]["stats"]:
                if stats["name"]=="runs":
                    print(f"The Angels scored {stats['value']} runs at home")
                    if int(stats["value"])>=7:
                        print("TRUE")
                    else:
                        print("FALSE")



def fetch_mlb_date(date):
    """

    Accepts a date and checks if the Angels played at home that day
    If they played at home it'll search for the game data otherwise it'll just do nothing
    You can review example data at:
    https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates=20240913

    """
    url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={date}"
    response = requests.get(url)
    
    # Check validity 
    if response.status_code<200 or response.status_code>300:
        raise LookupError

    if "@ LAA" not in str(response.content):
        raise LookupError

    # Search
    mlb_dict = json.loads(response.content)
    for key, events in mlb_dict.items():
        if key != "events":
            continue
        for event in events:
            cur_game_id = event.get("id")
            cur_short_name = event.get("shortName")
            if cur_short_name and " @ LAA" in cur_short_name:
                fetch_runs(cur_game_id)
                break

if __name__ == "__main__":
    date = sys.stdin.read().strip()
    fetch_mlb_date(date)