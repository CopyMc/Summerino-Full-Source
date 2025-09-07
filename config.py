import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("")
PREFIX = "!"
BOT_NAME = "Summerino Created By Copy"
VERSION = "2.0"


TENOR_API = os.getenv("TENOR_API")
OPENWEATHER_API = os.getenv("OPENWEATHER_API")


COLORS = {
    "success": 0x00FF00,
    "error": 0xFF0000,
    "warning": 0xFFD700,
    "info": 0x0099FF,
    "fun": 0xFF00FF
}


STARTING_BALANCE = 1000
DAILY_REWARD = 100
WORK_REWARD_MIN = 50
WORK_REWARD_MAX = 200