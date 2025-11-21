import requests
import os

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
nasa_api_key = os.getenv("NASA_API_KEY")

todays_api_call = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}")
title = todays_api_call.json()["title"]
image = todays_api_call.json()["hdurl"]
caption = todays_api_call.json()["explanation"]

caption = f"""
<b>🌅 Good Morning JB, today is a new day!</b>

<b>{title} 🚀💫🌍</b>

📝 <b>Description:</b>
{caption}
"""

requests.get(f"https://api.telegram.org/bot{bot_token}/sendPhoto", 
             params={
            "chat_id": chat_id,
            "photo": image,
            "caption": caption,
            "parse_mode": "HTML"
             }
    )
