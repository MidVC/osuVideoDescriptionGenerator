import os
from ossapi import Ossapi, Beatmap
from dotenv import load_dotenv

load_dotenv("../../.env.midc")

clientId = os.getenv("OAUTHCLIENTID")
clientSecret = os.getenv("OAUTHCLIENTSECRET")
api = Ossapi(clientId, clientSecret)

def handleMap(mapID: int) -> str :
    map = api.beatmap(beatmap_id=mapID)

    ans = "Map:https://osu.ppy.sh/beatmaps/" + str(mapID) + "\n"

    ans += "⭐" + "{:.2f}".format(map.difficulty_rating) + " | "
    ans += "{:.0f}".format(map.bpm) + "bpm | "
    ans += "AR: " + "{:.2f}".format(map.ar) + " | "
    ans += "CS: " + "{:.2f}".format(map.cs) + " | "
    ans += "OD: " + "{:.2f}".format(map.accuracy) + " | "
    ans += "HP: " + "{:.2f}".format(map.drain) + "\n"
    
    return ans

