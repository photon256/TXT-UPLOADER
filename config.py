import os

API_ID  = os.environ.get("API_ID", 16253557"")

API_HASH = os.environ.get("API_HASH", "81171c25e4cb9062cb10da8b7730432a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "1996039956"))

LOG = -1002373511813

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1996039956").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


