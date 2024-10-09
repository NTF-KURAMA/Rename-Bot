import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7769509314:AAEIxnQ34ja5KfJYEBF3S-GbBU18Eof-fmI")
ADMIN = int(os.environ.get("ADMIN", "7219138626"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002368029778"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Kurana:kurama@cluster0.dxbzy.mongodb.net/")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "CodeXBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
