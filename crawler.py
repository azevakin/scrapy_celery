from typing import List, Type

from scrapy import Spider
from scrapy.crawler import CrawlerProcess


def crawl_spider(spider: Type[Spider], urls: List[str]):
    crawler = CrawlerProcess()
    crawler.crawl(spider, start_urls=urls)
    crawler.start()
    crawler.stop()
