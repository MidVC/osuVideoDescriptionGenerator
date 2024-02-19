import os
import sys
from dotenv import load_dotenv
from .src.beatmapMode import handleBeatmapMode
from .src.playlinkMode import handlePlaylinkMode

load_dotenv('.env.example')

if __name__ == '__main__':

    mode = os.environ.get('MODE')

    if mode == 1:
        handleBeatmapMode()
    elif mode == 2:
        print("Playlink mode not available", file=sys.stderr)
        exit(0)

        handlePlaylinkMode()
    else:
        print("Wrong mode provided in .env!", file=sys.stderr)
        exit(0)
