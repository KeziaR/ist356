from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, timeout=60000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023//syllabus")
    

    headings = page.query_selector_all("h2, h3")
    for headers in headings:
        tag = headers.evaluate("el => el.tagName")
        title = headers.inner_text()
        if tag == "H3":    
            print(f"{tag}")
            print(headers.inner_text())
        elif tag == "H2":    
            print(f"{tag}")
            print(headers.inner_text())
        else:
            print(f"{title}")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)