from scrapy import Spider


class TestSpider(Spider):
    name = "test_spider"

    def parse(self, response, **kwargs):
        h1 = response.xpath("//h1").get()
        yield {
            "h1": h1
        }
