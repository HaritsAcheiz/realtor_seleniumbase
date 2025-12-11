from seleniumbase import SB
from dataclasses import dataclass


@dataclass
class RealtorSeleniumBase:
    base_url: str = "https://www.realtor.com"

    def scrape(self):
        with SB(headless=False, uc=True) as sb:
            sb.driver.uc_open_with_tab(self.base_url)
            print(sb.get_html())
            input("Press Enter to close...")

if __name__ == "__main__":
    scraper = RealtorSeleniumBase()
    scraper.scrape()

    
