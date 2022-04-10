import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # may be used instead of the start_requests_method

    def start_requests(self):
        urls = [
            'https://www.asos.com/de/herren/schuhe-stiefel-sneaker/cat/?cid=4209&nlid=mw%7Cschuhe%7Cnach%20produkt%20shoppen%7Calle%20anzeigen&page=2',
            'https://www.asos.com/de/damen/neu-in/cat/?cid=27108&ctaref=15offnewcustomer%7Cglobalbanner%7Cww&currentpricerange=0-530&refine=attribute_1047:8606'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        # get value of some css selector
        print(response.css('title::text').getall())

        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

