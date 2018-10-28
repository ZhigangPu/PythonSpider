import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BASESpider(scrapy.Spider):
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

class CRAWLSpider(CrawlSpider):
    name = "MLmastery_rules"
    start_urls = ['https://cloud.tencent.com/developer/articles/69']

    rules = (-
        Rule(LinkExtractor(allow=("/developer/article",)), callback='parse_article'),
    )

    def parse_article(self, response):
        page = response.url.split('/')[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.logger.info('Saved file %s' % filename)

class XMLFEEDSpider(scrapy.spiders.XMLFeedSpider):
    name = 'MLmainbody'
    start_urls = ['https://machinelearningmastery.com/how-to-grid-search-naive-methods-for-univariate-time-series-forecasting/']
    itertor = 'html'
    itertag = 'p'

    def parse_node(self, response, node):
        print(node.extract())
