# import scrapy
# import pandas as pd
# from scrapy.crawler import CrawlerProcess
#
# class autocjlinks(scrapy.Spider):
#     name = 'pagelinks'
#
#     start_urls = ['https://autocj.co.jp/used_cars?key=&sort=price&refno=&category=&ccto=&hv=']
#
#     def parse(self, response):
#         lst = []
#         for i in range(1,100):
#             next_page = 'https://autocj.co.jp/used_cars?category=&maker=&model=&fuel=&shift=&mileagefrom=&mileageto=&from=&to=&drive=&pfrom=&pto=&ccfrom=&ccto=&port=&key=&refno=&sort=&' \
#                         'page=' + str (i) + '&ken=&rse=&cnt=&psort=price14&sno=&pdfrom=&pdto=&other=#listtop'
#
#             lst.append(next_page)
#
#         # print(lst)
#         x = pd.DataFrame(lst,columns = ['urls'])
#         print(x)
#         yield {x.to_csv ('links.csv')}
#
# process = CrawlerProcess()
# process.crawl(autocjlinks)
# process.start()
