from ossapi import Ossapi, Score

def handlePlay(api:Ossapi, score:Score, position:int) -> str:
    return "#" + str(position) +\
        " global map rank, " +\
        "{:.2f}".format(score.pp) + "pp\n"
