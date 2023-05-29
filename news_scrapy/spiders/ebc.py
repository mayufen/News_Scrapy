from datetime import datetime

import bs4
import scrapy


class EbcSpider(scrapy.Spider):
    name = "ebc"
    allowed_domains = ["news.ebc.net.tw"]
    start_urls = ["https://news.ebc.net.tw/realtime?page=1"]

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        articles = soup.find_all('div', {'class': 'style1 white-box'})
        
        for article in articles:
            
            title = article.select_one('a').get('title')
            
            url = 'https://news.ebc.net.tw' + article.select_one('a').get('href')
            
            summary = article.find('span', {'class': 'summary'}).getText()
            
            date_str = article.find('span', {'class': 'small-gray-text'}).getText()
            date_with_year = str(datetime.now().year) + f'/{date_str}'
            date = datetime.strptime(date_with_year, "%Y/%m/%d %H:%M")

            print(date)