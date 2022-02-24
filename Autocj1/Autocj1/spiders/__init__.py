
import scrapy


class autocj (scrapy.Spider):
    name = "autocj"
    start_urls = ['https://autocj.co.jp/used_cars?key=&sort=price&refno=&category=&ccto=&hv=']
    allowed_domain = ['https://autocj.co.jp']

    def parse(self, response, **kwargs):
        for i in range (30):
           for x in response.xpath('//*[@id="stock-container"]/div[3]/ul/li['+str(i)+']/div[2]/h2/a/@href').extract():

               curl = 'https://autocj.co.jp/' + x  # Do not use [curl = self.base_url + x ]. str can't be concatenated.
               yield scrapy.Request(curl, callback = self.car_parse)


        for l in range(1,10):

           next_page = 'https://autocj.co.jp/used_cars?category=&maker=&model=&fuel=&shift=&mileagefrom=&mileageto=&from=&to=&drive=&pfrom=&pto=&ccfrom=&ccto=&port=&key=&refno=&sort=&page='+str(l)+'&ken=&rse=&cnt=&psort=price14&sno=&pdfrom=&pdto=&other=#listtop'

           yield response.follow(next_page,callback = self.parse)


    def car_parse(self, response):
        yield {
            # 'Name': response.xpath ('//*[@id="titlebox"]/div[1]/h1/text()').get (),
            # 'FOB price': response.xpath ('//*[@id="vbox"]/div[2]/div/div[1]/div[1]/dl/dd[2]/text()').get (),
            # 'original price': response.xpath ('//*[@id="vbox"]/div[2]/div/div[1]/div[1]/dl/dd[1]/span/text()').get (),
            # 'Reference price': response.xpath (
            #        '//*[@id="vbox"]/div[2]/div/div[1]/div[1]/dl/dd[3]/span[1]/text()').get (),
            'Ref No'    : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[1]/text()').get (),
            # 'Maker'     : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[2]/text()').get (),
            # 'Name_2'    : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[3]/text()').get (),
            # 'Grade'     : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[4]/text()').get (),
            # 'Model'     : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[5]/text()').get (),
            # 'Category'  : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[6]/text()').get (),
            # 'color'     : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[7]/text()').get (),
            # 'Ryear/Month': response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[8]/text()').get (),
            # 'P year'    : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[9]/text()').get (),
            # 'port'      : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[1]/dd[10]/text()').get (),
            # 'Mileage'   : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[1]/text()').get (),
            # 'C.C'       : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[2]/text()').get (),
            # 'Fuel'      : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[3]/text()').get (),
            # 'Door'      : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[4]/text()').get (),
            # 'Seat'      : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[5]/text()').get (),
            # 'Tramsmission': response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[6]/text()').get (),
            # 'Drive'     : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[7]/text()').get (),
            # 'Dimension(LWH)': response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[8]/text()').get (),
            # 'M3'        : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[9]/text()').get (),
            # 'Stereo'    : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[10]/text()').get (),
            # 'Tyre size' : response.xpath ('//*[@id="vbox"]/div[2]/div/div[2]/dl[2]/dd[11]/text()').get (),

        }













