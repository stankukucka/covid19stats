# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.http import Request

class Covid19Spider(Spider):
    name = 'covid19'
    allowed_domains = ['https://www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        table = response.xpath('//table[contains(@id, "main_table_countries_today")]')[0]
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
            country = tr.xpath('.//td[1]//text()').extract_first()
            totalcases = tr.xpath('.//td[2]//text()').extract_first()
            newcases = tr.xpath('.//td[3]//text()').extract_first()
            totaldeaths = tr.xpath('.//td[4]//text()').extract_first()
            newdeaths = tr.xpath('.//td[5]//text()').extract_first()
            totalrecovered = tr.xpath('.//td[6]//text()').extract_first()
            activecases = tr.xpath('.//td[7]//text()').extract_first()
            seriouscritical = tr.xpath('.//td[8]//text()').extract_first()
            totcases1mpop = tr.xpath('.//td[9]//text()').extract_first()
            totdeaths1mpop = tr.xpath('.//td[10]//text()').extract_first()

            yield {'country': country,
                   'totalcases': totalcases,
                   'newcases': newcases,
                   'totaldeaths': totaldeaths,
                   'newdeaths': newdeaths,
                   'totalrecovered': totalrecovered,
                   'activecases': activecases,
                   'seriouscritical': seriouscritical,
                   'totcases1mpop': totcases1mpop,
                   'totdeaths1mpop': totdeaths1mpop
            }
