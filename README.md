# Infinite Scrolling Scraper

This script is designed to scrape an infinite scrolling website using the Selenium library. It opens a Chrome web browser, navigates to the specified website, and continuously scrolls down the page until the entire webpage is loaded. The script then stores the page source and returns it.

## How to use
* Install the required libraries:
   * Selenium
   * webdriver_manager (optional, but recommended for easily installing the appropriate version of ChromeDriver)
* Create an instance of the InfiniteScrolling class, passing in the URL of the website you want to scrape as an argument.
* Call the scrolling_page_source() method on your instance to start the scraping process.
* The page source will be stored in the source attribute of your instance and returned by the method.
