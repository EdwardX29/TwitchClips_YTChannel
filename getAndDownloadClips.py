from twitchAPI.twitch import Twitch
from TwitchCredentials import client_id, client_secret
from datetime import datetime
import requests

# initialize Twitch client
twitch = Twitch(client_id, client_secret)


# date for the beginning date for searches
start_date_string = "2022-07-01" # Your start date here
start_date = datetime.strptime(start_date_string, "%Y-%m-%d", )

# date for the ending date for searches
end_date_string="2022-07-31" # Your end date here
end_date = datetime.strptime(end_date_string, "%Y-%m-%d", )

# get clip data
clips = twitch.get_clips("173758090", first=22, started_at=start_date,
                        ended_at=end_date)["data"]

# download all clips into clips/ folder
for id, clip in enumerate(clips):
    
    url = clip["thumbnail_url"].split("-preview-")[0] + ".mp4"

    if "offset" in url:
        url = "".join(url.split("AT-cm%7"))

    mp4_url = url
    content = requests.get(mp4_url).content 
    with open(f"clips/{id}.mp4", "wb") as f:
        f.write(content)
