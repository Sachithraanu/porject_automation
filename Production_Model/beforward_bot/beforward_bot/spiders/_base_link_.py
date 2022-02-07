import scrapy
import logging
import os
from twisted.python.failure import Failure
from scrapy.utils.request import referer_str

class MySpider(scrapy.Spider):
    name = 'beforward_1'
    start_urls = ['https://www.beforward.jp/']

    BASE_URL = 'https://www.beforward.jp'

    def parse(self, response):
        links = response.xpath('//a[contains(@href, "make")]/@href').extract()
        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_model)

    def parse_model(self, response):
        links_1 = response.css('a.vehicle-url-link::attr(href)').extract()
        for lin in links_1:
            absolute_url_1 = self.BASE_URL + lin
            yield scrapy.Request(absolute_url_1, callback=self.parse_model_1)

    def parse_model_1(self, response):
        # vehicles = response.xpath('//*[@id="list-content"]/div[3]')

        # for vehicle in vehicles:
            yield {
                    "Model": response.xpath('//*[@id="list-detail"]/div[2]/div[1]/div[1]/div/div/h1/text()').get(),
                    "Ref": response.xpath('//*[@id="list-detail"]/div[2]/div[1]/div[1]/div/div/div/div/text()').get(),
                    "Price": response.xpath('//*[@id="list-detail"]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/p[2]/span[2]/text()').get()
                    # "Model": response.xpath('normalize-space(//*[@id="list-content"]/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/div[1]/p/a/text())').get(),
                    # "Price": response.xpath('//*[@id="list-content"]/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]/div/a/div/div[1]/p[2]/span[2]/text()').get(),
                    # "Ref": response.xpath('//*[@id="list-content"]/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[1]/p/a/span/text()').get()
                    }

        # next_page = response.css('a.pagination-next').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
