import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VK_TOKEN = os.getenv("VK_TOKEN")
    ANTICAPTCHA_TOKEN = os.getenv("ANTICAPTCHA_TOKEN")
    VIP3_TOKEN = os.getenv("VIP3_TOKEN")
    VIEWER_ID = os.getenv("VIEWER_ID")
    GROUP_ID = os.getenv("GROUP_ID", "182985865")
    API_ID = os.getenv("API_ID", "7055214")
