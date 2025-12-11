from seleniumbase import SB
from dataclasses import dataclass
from selenium.webdriver.common.keys import Keys


@dataclass
class RealtorSeleniumBase:
    base_url: str = "https://www.realtor.com"

    def scrape(self, zipcode):
        with SB(headless=False, uc=True, page_load_strategy="eager") as sb:
            sb.uc_open(self.base_url)
            sb.wait_for_element('input#search-bar', by="css selector", timeout=10)
            sb.send_keys('input#search-bar', text=zipcode, by="css selector", timeout=10)
            sb.click('button[aria-label="Search"]', by="css selector", timeout=None, delay=0, scroll=True)
            print(sb.get_html())
            input("Press Enter to close...")

if __name__ == "__main__":
    # Parameters
    zipcode = '90001'
    
    scraper = RealtorSeleniumBase()
    scraper.scrape(zipcode)

    
