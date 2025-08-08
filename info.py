# info.py
import re
from Script import script

id_pattern = re.compile(r"^.\d+$")

def is_enabled(value, default):
    if isinstance(value, str):
        value = value.lower()
        if value in ["true", "yes", "1", "enable", "y"]:
            return True
        elif value in ["false", "no", "0", "disable", "n"]:
            return False
    return default

# Hardcoded values
SESSION = "Media_search"
API_ID = 23884743
API_HASH = "b8c26efa0bc0e98f306094ca676165d2"
#BOT_TOKEN ="8216289057:AAF-ciONTLn3fjMBrAM3wS_NYOu4Y5gPfoE" #Backup bot @FilmyswapMoviesBot
BOT_TOKEN="6440636978:AAEZWjxQFM0ul9_-jGJ50ogZJhp-aKPqzhQ"
PORT = "8082"

ADMINS = [6216066502]
OWNER_USERNAME = "Deb01admin" # only username
USERNAME = "Deb01admin" # only username
CONTACT_OWNER="https://t.me/Contact_Vicky_via_bot" # full link to contact user

CHANNELS = []
AUTH_CHANNEL = -1002575243889
AUTH_REQ_CHANNEL = -1002575243889
LOG_CHANNEL = -1002681917761
LOG_API_CHANNEL = 0
LOG_VR_CHANNEL = 0

DATABASE_URI = "mongodb+srv://debashishkuanr17:jmlUuZAYI5tZ7pzX@cluster0.lm1kn7c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "captions_db2"
FILES_DATABASE = DATABASE_URI
COLLECTION_NAME = "Vicky"

SUPPORT_GROUP = -1002655023543
DELETE_CHANNELS = 0
request_channel = "-1002678650823"
REQUEST_CHANNEL = int(request_channel) if id_pattern.search(request_channel) else None
MOVIE_UPDATE_CHANNEL = -1002358925714

SUPPORT_CHAT = "-1002655023543" # this variable was not used in the code !!
MOVIE_GROUP_LINK = "https://t.me/+Rh6MeSC3FkhhOTRl"

IS_VERIFY = False

TUTORIAL = "https://t.me/"
TUTORIAL_2 = "https://t.me/"
TUTORIAL_3 = "https://t.me/"
VERIFY_IMG = "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"
SHORTENER_API = "3097623f852197a9ce40d1212aaa8bbf2803e799"
SHORTENER_WEBSITE = "omegalinks.in"
SHORTENER_API2 = "3097623f852197a9ce40d1212aaa8bbf2803e799"
SHORTENER_WEBSITE2 = "omegalinks.in"
SHORTENER_API3 = "3097623f852197a9ce40d1212aaa8bbf2803e799"
SHORTENER_WEBSITE3 = "omegalinks.in"
TWO_VERIFY_GAP = 14400
THREE_VERIFY_GAP = 14400

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi", "marathi"]
QUALITIES = ["HdRip", "web-dl", "bluray", "hdr", "fhd", "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f"{i}" for i in range(2025, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]


#https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2trajF5eThxN2h5d2kzaXl6aTZ5MWhpbWEya2doNjBnbGtvMnZiYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PnoQLaOLYp93ebw382/giphy.gif"
START_IMG = ["https://ibb.co/mrfjj8KW"]
FORCESUB_IMG = "https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg"
REFER_PICS = "https://graph.org/file/1a2e64aee3d4d10edd930.jpg"
PAYPICS = ["https://ibb.co/YBSqKK3J"] #["https://graph.org/file/f4db1c3ad3d9e38b328e6.jpg"]
#SUBSCRIPTION = "https://ibb.co/1fwc90Pp"
SUBSCRIPTION="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2trajF5eThxN2h5d2kzaXl6aTZ5MWhpbWEya2doNjBnbGtvMnZiYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PnoQLaOLYp93ebw382/giphy.gif"#

REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
START_STICKER_ID=["CAACAgEAAxkBDUQslWiTkD49Ni1EqyhUxWGwMYrpDWJuAALBAQACbdJQRUHYYW_kG1PNNgQ",
               "CAACAgUAAx0CZz_GMwACMBdnXZA4SejgJ6a_0TrNzOfn9ImI_QACNwsAArT4iFVaZPJf8ldVVh4E",
               "CAACAgEAAxkBDUQsoWiTkEOkcFKgS6tBSvuie8pMt1WgAALBAgACwe4hRMlWvZyd07lbNgQ",
               "CAACAgUAAxkBDURG1miTmcSLoXM6amyuAAHJCsF_2YhIJAACPgkAAs4vkVVp-07Hcmam-zYE",
               "CAACAgUAAxkBDURG12iTmca6N4MwrCPdBj6Yg8jMfTNlAAIZCAACTyTJVg0m-XQjRkvJNgQ",
               "CAACAgIAAxkBDUQvI2iTkS9MlTvJ6cZCNcttmM6GcPbNAAK-BQACP5XMCpuPAohdSwctNgQ",
               "CAACAgIAAyEFAASg-nN3AAIN8miTaViPlbam-d-uHSTLfVENdxpLAALTBQACP5XMCp9au9JdR8cxNgQ",
               "CAACAgIAAxkBDUQq6GiTj51SX_MZbrk6BwbZ2Q3A_gqiAAKOFQACJU3BSY8WTX7r0TbzNgQ",
               ]

AUTO_FILTER = True
IS_PM_SEARCH = True
IS_SEND_MOVIE_UPDATE = True
MAX_BTN = 8
AUTO_DELETE = True
DELETE_TIME = 1200
FILE_AUTO_DEL_TIMER = None
IMDB = False
FILE_CAPTION = script.FILE_CAPTION
IMDB_TEMPLATE = script.IMDB_TEMPLATE_TXT
LONG_IMDB_DESCRIPTION = False
PROTECT_CONTENT = True
SPELL_CHECK = True
LINK_MODE = True
TMDB_API_KEY = ""
STREAM_MODE = True

MULTI_CLIENT = True
SLEEP_THRESHOLD = 60
PING_INTERVAL = 1200
ON_HEROKU = False
URL = "https://telegram-streaming-bot-vicky17-5ba81cfa.koyeb.app/"



PREMIUM_POINT=None #integer value used in user_chats_db.py at line 87
REF_PREMIUM=None #integer value used in user_chats_db.py at line 88

admin_cmds = [
    "/add_premium - Add A User To Premium",
    "/premium_users - View All Premium Users",
    "/remove_premium - Remove A User's Premium Status",
    "/add_redeem - Generate A Redeem Code",
    "/refresh - Refresh Free Trail",
    "/set_muc - Set Movie Update Channel",
    "/pm_search_on - Enable PM Search",
    "/pm_search_off - Disable PM Search",
    "/set_ads - Set Advertisements",
    "/del_ads - Delete Advertisements",
    "/setlist - Set Top Trending List",
    "/clearlist - Clear Top Trending List",
    "/verify_id - Verification Off ID",
    "/index - Index Files",
    "/send - Send Message To A User",
    "/leave - Leave A Group Or Channel",
    "/ban - Ban A User",
    "/unban - Unban A User",
    "/broadcast - Broadcast Message",
    "/grp_broadcast - Broadcast Messages To Groups",
    "/delreq - Delete Join Request",
    "/channel - List Of Database Channels",
    "/del_file - Delete A Specific File",
    "/delete - Delete A File(By Reply)",
    "/deletefiles - Delete Multiple Files",
    "/deleteall - Delete All Files",
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"},
]
