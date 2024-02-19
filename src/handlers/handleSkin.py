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
        return HDDTSKIN
    elif ("DT" in mods) or ("NC" in mods):
        return DTSKIN
    elif ("HR" in mods) and ("HD" in mods):
        return HDHRSKIN
    elif ("HR" in mods):
        return HRSKIN
    elif ("HD" in mods):
        return HDHRSKIN
    elif ("EZ" in mods):
        return EZSKIN
    else: 
        return NMSKIN
    
