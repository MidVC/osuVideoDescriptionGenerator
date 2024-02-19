import os
from ossapi import Ossapi, BeatmapUserScore
import handlers
from dotenv import load_dotenv

load_dotenv('../.env.midc')

clientId = os.getenv("OAUTHCLIENTID")
clientSecret = os.getenv("OAUTHCLIENTSECRET")
api = Ossapi(clientId, clientSecret)

userId = os.getenv("OSUUSERID")

def handleBeatmapMode():
    beatmapId = input("Please input beatmap ID: ")
    beatmapScore = api.beatmap_user_score(beatmap_id=beatmapId, user_id=userId)

    ans = ""
    ans += handlers.handlePlay(api, beatmapScore.score)
    ans += handlers.handlePlayer(api, userId)
    ans += handlers.handleSkin(beatmapScore.score.mods.short_name())
    ans += handlers.handleMap(api, beatmapId, beatmapScore.score.mods)

    return ans

print(handleBeatmapMode())
