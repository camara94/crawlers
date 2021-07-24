from scrapy import Request, Spider
from ..items import ArticleItem
from jumia import items


class SpiderArticle(Spider):
    name = "article"
    url = "https://www.jumia.com.tn/"

    def start_requests(self):
        yield Request(url=self.url,  callback=self.parse_article)

    def parse_article(self, response):
        listArticle = response.css('article.prd')
        for article in listArticle:
            designation = article.css('div.name::text').extract_first()
            image = article.css('img.img').attrib['data-src']
            prix = article.css('div.prc::text').extract_first()
            pourcent = article.css('div.tag::text').extract_first()

            item = ArticleItem()

            item['designation'] = designation
            item['image'] = image
            item['prix'] = prix
            item['pourcent'] = pourcent

            yield item
