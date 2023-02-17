from multiprocessing import Process
from typing import List

from celery_app import celery_app
from crawler import crawl_spider
from spiders import EnnergiiaSpider


@celery_app.task()
def run_spider(links: List[str]):
    p = Process(target=crawl_spider, args=(EnnergiiaSpider, links))
    p.start()
    p.join()
