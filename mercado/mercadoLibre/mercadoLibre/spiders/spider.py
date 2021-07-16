import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from .. items import MercadolibreItem

class MercadoSpider(CrawlSpider):
    name = "mercado"
    item_count = 0
    start_urls = ["https://computacion.mercadolibre.com.ar/impresion/impresoras/"]
    allowed_domain = ["https://www.mercadolibre.com.ar/"]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    #coloco reglas de extraccion uso xpath
    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=("//li[@class='andes-pagination__button andes-pagination__button--next']/a") )),
        Rule(LinkExtractor(allow=(), restrict_xpaths=("//h2[@class='ui-search-item__title']")), callback="parse_item", follow = False)
    }

    def parse_item(self, response):
        mi_item = MercadolibreItem()
        #info del producto son los field que declare antes
        #normalize spaces le saca los espacios
        print("Llego")
        mi_item['titulo'] = response.xpath('normalize-spaces("//*[@id="root-app"]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/h1")")').extract()
        mi_item['folio'] = response.xpath('//*[@id="root-app"]/div[2]/div[3]/div[1]/div[2]/div[1]/form/div[2]/div/div/p[2]').extract()
        mi_item['precio'] = response.xpath('//span[@class="price-tag-fraction"][0]').extract()
        mi_item['condicion'] = response.xpath('//*[@id="root-app"]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span').extract()
        print("Llego")
        #uso contains porque tiene 2 clases ui-pdp-color--GREEN ui-pdp-media__title
        mi_item['envio'] = response.xpath('//*[contains(@class, "ui-pdp-media__title")/text()]').extract()
        mi_item['opiniones'] = response.xpath('//h2[@class="ui-pdp-reviews__rating__summary__average"').extract()
        # mi_item['venta_producto'] = response.xpath('//*[@id="root-app"]/div[2]/div[3]/div[1]/div[2]/div[1]/form/div[2]/div/div/p[2]').extract()
        # mi_item['folio'] = response.xpath('//*[@id="root-app"]/div[2]/div[3]/div[1]/div[2]/div[1]/form/div[2]/div/div/p[2]').extract()
        print("Llego")
        self.item_count += 1
        if self.item_count > 20:
            raise CloseSpider("item_exceeded")
        yield mi_item