import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://dolarhoy.com/",
    ]

    def parse(self, response):
        titulos=response.xpath('//div[@class="tile is-child"]/a[@class="title"]/text()').getall()
        compras=response.xpath('//div[@class="tile is-child"]/div[@class="values"]/div[@class="compra"]/div[@class="val"]/text()').getall()
        ventas=response.xpath('//div[@class="tile is-child"]/div[@class="values"]/div[@class="venta"]/div[@class="val"]/text()').getall()
        
        for i in titulos:
            if i != 'Dólar Tarjeta':
                yield {
                    'dolar': titulos[i],
                    'compra': compras[i],
                    'venta': ventas[i],
                }
            else:
                yield {
                    'dolar': titulos[i],
                    'venta': ventas[i],
                }
