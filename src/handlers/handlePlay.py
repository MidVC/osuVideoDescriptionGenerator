from ossapi import Ossapi, Score

def handlePlay(api:Ossapi, score:Score) -> str:
    return "#" + str(score.rank_global) +\
        " global (#" + str(score.rank_country) + " CN) map rank, " +\
        "{:.2f}".format(score.pp) + "pp\n"
