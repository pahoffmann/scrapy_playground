import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # may be used instead of the start_requests_method
    """start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]"""

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        quotes = response.css(".quote");
        for quote in quotes:
            yield {
                'tags': quote.css("div.tags a.tag::text").getall(),
                'text': quote.css("span.text::text").get(),
                'author': quote.css("small.author::text").get()
            }

            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
