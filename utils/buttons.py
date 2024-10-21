import asyncio
from pyppeteer import launch
import time

def buttons_getter(vk_session) -> list: 
    sorted_buttons_temp = []
    message = vk_session.get_api().messages.getConversationsById(peer_ids = -182985865)
    if 'current_keyboard' in message['items'][0]:
        all_buttons = message['items'][0]['current_keyboard']['buttons']
        for current_button in all_buttons:
            for button_property in range(len(current_button)):
                current_button_name = current_button[button_property]['action']['label']
                current_button_type = current_button[button_property]['color']
                current_button_payload = current_button[button_property]['action']['payload']
                sorted_buttons_temp.append((current_button_name.lower(), current_button_type.lower(), current_button_payload))
        return sorted_buttons_temp
    return []
            
def press_button(url: str, selector: str):
    async def get_page_content(url, selector):
        browser = await launch(args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto(url)
        time.sleep(5)
        await page.click(f'{selector}')
        await browser.close()
    asyncio.get_event_loop().run_until_complete(get_page_content(url, selector))



