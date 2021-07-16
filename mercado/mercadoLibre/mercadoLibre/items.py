# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadolibreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # vamos a sacar titulo, folio, precio, condicion
    titulo = scrapy.Field()
    folio = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    opiniones = scrapy.Field()