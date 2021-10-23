import asyncio
from pyppeteer import launch
import inspect

URL = "https://ourworldindata.org/grapher/health-expenditure-and-financing-per-capita?tab=table"


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(URL)
    await page.waitFor(10 * 1000)
    content = await page.content()

    print(content)

    # for i in out:
    #     print(i)

    # __call__
    # __class__
    # __delattr__
    # __dir__
    # __doc__
    # __eq__
    # __format__
    # __func__
    # __ge__
    # __get__
    # __getattribute__
    # __gt__
    # __hash__
    # __init__
    # __init_subclass__
    # __le__
    # __lt__
    # __ne__
    # __new__
    # __reduce__
    # __reduce_ex__
    # __repr__
    # __self__
    # __setattr__
    # __sizeof__
    # __str__
    # __subclasshook__



    await browser.close()

asyncio.get_event_loop().run_until_complete(main())