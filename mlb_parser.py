import requests
from datetime import datetime


cur_date_str = datetime.now().strftime('%Y%m%d')
url = f"https://www.espn.com/mlb/scoreboard/_/date/{cur_date_str}"

# Test URL
url = "https://www.espn.com/mlb/scoreboard/_/date/20230627"

headers = {
    'User-Agent': 'Safari/537.36'
}

response = requests.get(url, headers=headers)

print(response.text)