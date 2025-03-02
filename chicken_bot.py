import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

payload = {
    "content": "TEST"
}

headers = {
    "Authorization": f"Bot {TOKEN}"
}

response = requests.post(url, json=payload, headers=headers)
