from ossapi import Ossapi

def handlePlayer(api: Ossapi, playerId: int) -> str :
    user = api.user(user=playerId)
    ans = "Player: https://osu.ppy.sh/u/"
    ans += str(playerId) + "\n"

    ans += "Username: " + user.username + "\n"

    ans += "{:.2f}".format(user.statistics.pp) + "pp, "
    ans += "#" + str(user.statistics.global_rank) + " global (#"
    ans += str(user.statistics.country_rank) + " " + user.country_code + ")\n"

    return ans
    
