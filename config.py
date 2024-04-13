import os

API_ID = API_ID = 7079281891

API_HASH = os.environ.get("API_HASH", "4981c2699bd91c7db836ec8f77e5b0f0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7079281891:AAE-56drZOSRWpGm883hIG1GExBc54hcNzY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1783306092))

LOG = -1002013842894

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


