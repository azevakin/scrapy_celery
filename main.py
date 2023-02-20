from tasks import run_spider


if __name__ == "__main__":
    run_spider.delay(
        spider_name="test_spider",
        links=[
            "https://docs.scrapy.org/en/latest/index.html",
            "https://docs.scrapy.org/en/latest/topics/spiders.html",
        ]
    )
