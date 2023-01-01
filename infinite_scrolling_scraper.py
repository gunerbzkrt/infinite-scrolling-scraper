from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class InfiniteScrolling:
    def __init__(self, website):
        # The website URL to scrape.
        self.website = website
        # The screen_height represents the entire height of the screen.
        self.screen_height = 0
        # The webpage_height represents the entire height of the web page.
        self.webpage_height = 0
        self.scroll_pause_time = 1
        self.source = []

    def scrolling_page_source(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.website)
        time.sleep(3)
        self.screen_height = driver.execute_script("return window.screen.height;")
        i = 1
        while True:
            driver.execute_script(f"window.scrollTo(0, {self.screen_height}*{i});")
            i += 1
            time.sleep(self.scroll_pause_time)
            self.webpage_height = driver.execute_script("return document.body.scrollHeight;")
            if self.screen_height * i > self.webpage_height:
                break
        self.source = driver.page_source
        return self.source
