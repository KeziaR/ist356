from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd

def scrape_Finance(playwright: Playwright, symbol:str, date:str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://finance.yahoo.com/quote/{symbol}")

    price_selector = page.query_selector("fin-streamer.livePrice")
    price = price_selector.inner_text()
    print(symbol, price)


    
    # ---------------------
    context.close()
    browser.close()

    return {
        "symbol": symbol,
        "price": price,
        "date" : date
    }


with sync_playwright() as playwright:

    portfolio = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]

    port_df = []
    
    for symbol in portfolio:
        sym_data = scrape_Finance(playwright, symbol, "2024-11-11")
        print(sym_data)
  
    df = pd.DataFrame(port_df)
    df.to_csv("./5-web/cache/portfolio_data.csv", index = False)

