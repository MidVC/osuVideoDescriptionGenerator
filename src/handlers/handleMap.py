from ossapi import Ossapi, Beatmap, Mod

def handleMap(api: Ossapi, mapID: int, mods:Mod) -> str :

    map = api.beatmap(beatmap_id=mapID)
    diff = api.beatmap_attributes(beatmap_id=mapID, mods=mods, ruleset="osu").attributes

    ans = "Map:https://osu.ppy.sh/b/" + str(mapID) + "\n"

    ans += "⭐" + "{:.2f}".format(diff.star_rating) + " | "
    if (("DT" in mods.short_name()) or ("NC" in mods.short_name())):
        ans += "{:.0f}".format(map.bpm * 1.5) + "bpm | "
    else:
        ans += "{:.0f}".format(map.bpm) + "bpm | "
    ans += "AR: " + "{:.2f}".format(diff.approach_rate) + " | "
    ans += "CS: " + "{:.2f}".format(map.cs) + " | "
    ans += "OD: " + "{:.2f}".format(diff.overall_difficulty) + " | "
    ans += "HP: " + "{:.2f}".format(map.drain) + "\n"

    return ans

