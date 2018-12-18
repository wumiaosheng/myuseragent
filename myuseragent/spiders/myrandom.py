# -*- coding: utf-8 -*-
import scrapy


class MyrandomSpider(scrapy.Spider):
    name = 'myrandom'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.request)
        print("***"*50)
        print(response.request.headers['User-Agent'])
        print("***" * 50)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
