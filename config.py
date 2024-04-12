import os

API_ID = API_ID = 1783306092

API_HASH = os.environ.get("API_HASH", "4981c2699bd91c7db836ec8f77e5b0f0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6795071444:AAELig0h2YS7BJPBpYi0G4S5bMym0L_FQR8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1783306092))

LOG = -1002109193587

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6989712278").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


