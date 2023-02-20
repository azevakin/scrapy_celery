from multiprocessing import Process
from typing import List

from celery_app import celery_app
from crawler import crawl_spider


@celery_app.task()
def run_spider(spider_name: str, links: List[str]):
    p = Process(target=crawl_spider, args=(spider_name, links))
    p.start()
    p.join()
