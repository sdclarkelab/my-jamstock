from urllib.parse import urljoin


class Scraper:
    BASE_URL = 'https://www.example.com'
    MARKETS = ["main-market", "junior-market", "usd-equities", "bond-market"]

    def scrape_listed_companies(self, retry_num=2):
        pass

    @staticmethod
    def get_listed_companies_url():
        listed_stocks_url = "/listings/listed-companies/?market={}"

        listed_companies_market_urls = []

        for market in Scraper.MARKETS:
            listed_companies_market_urls.append(urljoin(Scraper.BASE_URL, listed_stocks_url.format(market)))

        return listed_companies_market_urls
