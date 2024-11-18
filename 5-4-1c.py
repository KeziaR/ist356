import re
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
import pandas as pd

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = f"https://newyork.craigslist.org/search/jsy/sss?free=1&query={search}#search=1~list~0~0"
    page.goto(url)
    sleep(5)
    #_______________________________
    listings_selector = page.query_selector("div.results")
    items = listings_selector.page.query_selector_all("div.results-node")
    scraped = []
    for item in items:
        title = item.query_selector("span.label").inner_text()
        price = item.query_selector("span.priceinfo").inner_text()
        if price: 
            price_text = price.inner_text()
        else:
            price_text = "N/A"
        print(title, "|", price,)
        scraped_item = {
            "title": title,
            "price": price_text,
            "loc": "NewJersey",
            "search": search
        }
        scraped.append(scraped_item)

    # ---------------------
    context.close()
    browser.close()

    df = pd.DataFrame(scraped)
    df.to_csv(f"./5-web/cache/craigslist_data_{search}.csv", index=False)

    search = input()
    with sync_playwright() as playwright:
        run(playwright, "sports equipment")