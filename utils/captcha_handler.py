import os
from python3_anticaptcha import ImageToTextTask
from dotenv import load_dotenv

def captcha_handler(captcha):
    load_dotenv()
    ANTICAPTCHA_TOKEN = os.getenv("GAME_CHAT_ID")
    key = ImageToTextTask.ImageToTextTask(
        anticaptcha_key=ANTICAPTCHA_TOKEN, save_format='const'
    ).captcha_handler(
        captcha_link=captcha.get_url()
        )
    return captcha.try_again(key['solution']['text'])