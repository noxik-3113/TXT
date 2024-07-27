import os

API_ID = API_ID = 3898167

API_HASH = os.environ.get("API_HASH", "4c58ba87f53bfc8d15f589daa8e4fa55")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7257788373:AAF7Y5xYWTzoysoyehb3Ie1nuWWAJ4pA0R0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1016931712))

LOG = -1002155970813

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7257788373").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
