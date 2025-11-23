import requests
import os

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
nasa_api_key = os.getenv("NASA_API_KEY")

todays_api_call = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}")
image = todays_api_call.json()["url"]
title = todays_api_call.json()["title"]
caption = todays_api_call.json()["explanation"]

if len(caption) > 1000:

    image_msg = f"""<b>🌅 Good Morning JB, today is a new day!</b>"""

    text_msg = f"""<b>{title} 🚀💫🌍</b>

📝 <b>Description:</b>
{caption}
    """

    send_img = requests.get(f"https://api.telegram.org/bot{bot_token}/sendPhoto", 
                params={
                "chat_id": chat_id,
                "photo": image,
                "caption": image_msg,
                "parse_mode": "HTML"
                }
        )

    send_caption = requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage",
                                params={
                                    "chat_id": chat_id,
                                    "text": text_msg,
                                    "parse_mode": "HTML"
                                }
    )

else:
    msg = f"""<b>🌅 Good Morning JB, today is a new day!</b>

<b>{title}🚀💫🌍</b>

<b>📝 Description: </b>
{caption}
    """
    send_img = requests.get(f"https://api.telegram.org/bot{bot_token}/sendPhoto", 
            params={
            "chat_id": chat_id,
            "photo": image,
            "caption": msg,
            "parse_mode": "HTML"
            }
    )

