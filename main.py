import os
import sys
from dotenv import load_dotenv
load_dotenv('.env.midc')

from src.beatmapMode import handleBeatmapMode
# from src.playlinkMode import handlePlaylinkMode


if __name__ == '__main__':

    mode = int(os.environ.get('MODE'))

    if mode == 1:
        handleBeatmapMode()
        exit(0)
    elif mode == 2:
        print("Playlink mode not available", file=sys.stderr)
        exit(0)
    else:
        print("Wrong mode provided in .env!", file=sys.stderr)
        exit(0)
