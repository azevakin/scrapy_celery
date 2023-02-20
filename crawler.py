from typing import List

from scrapy.crawler import CrawlerProcess


def crawl_spider(spider_name: str, urls: List[str]):
    crawler = CrawlerProcess(settings={
        "SPIDER_MODULES": ["spiders"],
        "FEEDS": {
            "items.jsonl": {"format": "jsonl"},
        },
    })
    crawler.crawl(spider_name, start_urls=urls)
    crawler.start()
    crawler.stop()
