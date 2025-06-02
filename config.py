import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7285235045:AAHr2u01d4zEY_vimFa1PUfXJReJJK_GJ20")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "25566754"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "27609daf8ee847978797a359024e7607")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "2073438175").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "SACHIN 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
