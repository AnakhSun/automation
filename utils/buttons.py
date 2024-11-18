import asyncio
from pyppeteer import launch
import time
            
def press_button(url: str, selector: str):
    async def get_page_content(url, selector):
        browser = await launch(args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto(url)
        time.sleep(5)
        await page.click(f'{selector}')
        await browser.close()
    asyncio.get_event_loop().run_until_complete(get_page_content(url, selector))
