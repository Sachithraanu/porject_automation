import scrapy
import logging
import os
from twisted.python.failure import Failure
from scrapy.utils.request import referer_str

class MySpider(scrapy.Spider):
    name = 'beforward'
    start_urls = ['https://www.beforward.jp/']

    def parse(self, response):
        for link in response.xpath('//a[contains(@href, "make")]/@href'):
            yield response.follow(link.get(), callback=self.parse_make)

    def parse_make(self, response):
        for i in range(30):
            for links in response.xpath('//*[@id="list-content"]/div[3]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/div[1]/p/a/@href'):
                yield response.follow(links.get(), callback=self.parse_model)

    def parse_model(self, response):
        vehicles = response.xpath('//*[@id="content"]')

        for vehicle in vehicles:
            yield {

                "Model": vehicle.xpath('//*[@id="list-detail"]/div[2]/div[1]/div[1]/div/div/h1/text()').get(),
                "Price": vehicle.xpath('//*[@id="list-detail"]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/p[2]/span[2]/text()').get()

            }





        # next_page = response.css('a.pagination-next').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)

