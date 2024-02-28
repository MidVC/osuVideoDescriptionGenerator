import os
from ossapi import Ossapi, Score, Beatmap, User, mod
import src.handlers as handlers
from dotenv import load_dotenv

load_dotenv('../.env.midc')

clientId = os.getenv("OAUTHCLIENTID")
clientSecret = os.getenv("OAUTHCLIENTSECRET")
api = Ossapi(clientId, clientSecret)

# unavailable due to API issue
def handlePlaylinkMode(playId: int) -> str:

    # Get the score and IDs we need
    score: Score = api.score(mode="osu", score_id=playId)
    beatmapId = score.beatmap.id
    playerId = score.user_id
    mods = score.mods.short_name()

    return handlers.handlePlay(api, playId) + "\n" + \
        handlers.handlePlayer(api, playerId) + "\n" + \
        handlers.handleSkin(api, mods) + "\n" + \
        handlers.handleMap(api, beatmapId)
        
print(handlePlaylinkMode(3034573))
