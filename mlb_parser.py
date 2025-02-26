import requests
import json

def fetch_scoreboard(date):
    url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={date}"
    response = requests.get(url)
    
    # Check validity 
    if response.status_code<200 or response.status_code>300:
        raise LookupError

    if "@ LAA" not in str(response.content):
        raise LookupError

    # Search
    mlb_dict = json.loads(response.content)
    counter=False
    for key, val in mlb_dict.items():
        print(key)
        print(type(val), len(val))
        for i in val:
            for key2, val2 in i.items():
                if key2=="id":
                    cur_id = val2
                if key2=="shortName" and  " @ LAA" in val2:
                    print(val2, cur_id)
    
    print(len(mlb_dict))

# Check the scoreboard for a specific date
fetch_scoreboard("20240913")

# url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary?event=401570673"
# response = requests.get(url)
# print(response.content)