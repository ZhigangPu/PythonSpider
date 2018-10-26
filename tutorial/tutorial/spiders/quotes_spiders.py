import scrapy

class QuotesSpider(scrapy.Spider):
    name = "MLmastery"

    def start_requests(self):
        urls = [
                'https://machinelearningmastery.com/blog/',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_link)
        
    def parse_link(self, response):
        article_urls = response.xpath('//section[@id="main"]//article/a/@href').extract()
        for url in article_urls:
            yield scrapy.Request(url, callback=self.parse_article)
            
    def parse_article(self, response):
        page = response.url.split('/')[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.logger.info('Saved file %s' % filename)
        