import os
from ossapi import Ossapi, Beatmap

clientId = os.getenv("OAUTHCLIENTID")
clientSecret = os.getenv("OAUTHCLIENTSECRET")
api = Ossapi(clientId, clientSecret)


def handlePlaylinkMode():
    pass
