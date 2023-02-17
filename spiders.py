from scrapy import Spider


class EnnergiiaSpider(Spider):
    name = "Ennergiia"

    def parse(self, response, **kwargs):
        h1 = response.xpath("//h1").get()
        yield {
            "h1": h1
        }
