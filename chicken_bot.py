import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
image_path = "assets/rendoners.png"

url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

with open(image_path, "rb") as file:

    payload = {
        "file": file
    }

    headers = {
        "Authorization": f"Bot {TOKEN}"
    }

    response = requests.post(url, files=payload, headers=headers)

