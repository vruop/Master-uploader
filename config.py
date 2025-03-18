import os

class Config(object):
    BOT_TOKEN = os.environ.get("7756457260:AAFQPEAIH4Dh-OLf3sGCGAfUzGfuWiVMyAc")
    API_ID = int(os.environ.get("22581733"))
    API_HASH = os.environ.get("1db7bdcf908100cc641c6a5276765c3d")
    AUTH_USER = os.environ.get('AUTH_USERS', '6530997270').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = ""
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
