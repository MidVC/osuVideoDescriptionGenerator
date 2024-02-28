from ossapi import Ossapi
import os

HDDTSKIN = os.getenv("HDDTSKIN")
DTSKIN = os.getenv("DTSKIN")
HRSKIN = os.getenv("HRSKIN")
NMSKIN = os.getenv("NMSKIN")
EZSKIN = os.getenv("EZSKIN")
HDSKIN = os.getenv("HDSKIN")
HDHRSKIN = os.getenv("HDHRSKIN")

def handleSkin(mods: str) -> str:
    if ("HD" in mods) and (("DT" in mods) or ("NC" in mods)):
        return "Skin: " + HDDTSKIN + "\n"
    elif ("DT" in mods) or ("NC" in mods):
        return "Skin: " + DTSKIN + "\n"
    elif ("HR" in mods) and ("HD" in mods):
        return "Skin: " + HDHRSKIN + "\n"
    elif ("HR" in mods):
        return "Skin: " + HRSKIN + "\n"
    elif ("HD" in mods):
        return "Skin: " + HDHRSKIN + "\n"
    elif ("EZ" in mods):
        return "Skin: " + EZSKIN + "\n"
    else: 
        return "Skin: " + NMSKIN + "\n"
    
