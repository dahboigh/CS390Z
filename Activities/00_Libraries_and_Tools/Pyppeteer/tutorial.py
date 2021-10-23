import asyncio
from pyppeteer import launch

# https://medium.com/analytics-vidhya/web-scrapping-using-pyppeteer-and-jupyter-notebook-69b07a6f914c

URL = 'https://play.google.com/store/apps/details?id=com.gamedevjr.crystalguardian'


async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(URL)
    # await page.waitFor(10 * 1000)

    element = await page.querySelectorAll('a.hrTbp ')

    for e in element:
        title = await page.evaluate('(element) => element.textContent', e)

        if title == 'View Details':
            await e.click()
            await page.waitForSelector('div.miUA7')
            permission_dict = {}
            while True:
                try:
                    app_name_obj = await page.querySelector('div.miUA7')
                    app_name = await page.evaluate('(element) => element.textContent', app_name_obj)
                    permission_dict.update({'app_name': app_name})
                    permission = await page.querySelectorAll('div.itQHhe')

                    for p in permission:
                        permission_title_obj = await p.querySelector('span.SoUQc')
                        permission_title_text = await p.evaluate('(element) => element.textContent', permission_title_obj)
                        permission_detail = await p.querySelectorAll('li.BCMWSd')
                        permission_detail_list = []

                        for pd in permission_detail:
                            permission_details = await page.evaluate('(element) => element.textContent', pd)
                            permission_detail_list.append(permission_details)
                            print(permission_title_text, ":", permission_detail_list)
                        permission_dict.update({permission_title_text: permission_detail_list})
                    break
                except:
                    pass
            break

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
