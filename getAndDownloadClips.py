# Updated to newest Twitch API version
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
from TwitchCredentials import client_id, client_secret
from datetime import datetime
import requests 

async def main():
    twitch = await Twitch(client_id, client_secret)
    user = await first(twitch.get_users(logins='CLIX'))

    print(user.id)

    start_date_string = "2023-12-01" # Your start date here

    start_date = datetime.strptime(start_date_string, "%Y-%m-%d", )

    end_date_string="2023-12-31" # Your end date here
    end_date = datetime.strptime(end_date_string, "%Y-%m-%d", )
    
    clips = twitch.get_clips(user.id, first=20, started_at=start_date, ended_at=end_date)
    
    i = 0
    arr = []
    async for clip in clips:
        i += 1
        print(clip.thumbnail_url)
        print(clip.url)
        print(clip.view_count)
        arr.append(clip)
        if i == 20:
            break
    
    for id, clip in enumerate(arr):
        url = clip.thumbnail_url.split("-preview-")[0] + ".mp4"

        if "offset" in url:
            print("here")
            url = "".join(url.split("AT-cm%7"))

        mp4_url = url
        content = requests.get(mp4_url).content 
        with open(f"clips/{id}.mp4", "wb") as f:
            f.write(content)



if __name__ == "__main__":
    asyncio.run(main())
