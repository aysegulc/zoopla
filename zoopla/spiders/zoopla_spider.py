# -*- coding: utf-8 -*-
import scrapy
from zoopla.items import ZooplaItem


class ZooplaSpider(scrapy.Spider):
    name = 'zoopla'
    allowed_domains = ['zoopla.co.uk']
    # start_urls = ['http://zoopla.co.uk/']

    def start_requests(self):
        try:
            zip_list = [i.strip() for i in self.zipcode.split(',')]
        except Exception:
            zip_list = []

        for i in zip_list:
            request = scrapy.Request('https://www.zoopla.co.uk/find-agents/estate-agents/' + i, self.parse)
            yield request

    def parse(self, response):
        item_links = response.xpath('//h2/a[@itemprop="url"]/@href').extract()
        for item in item_links:
            yield scrapy.Request(response.urljoin(item), self.parse_branch)

        next_page = response.xpath('//a[text()="Next"]/@href').extract_first(default='')
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), self.parse)

    def parse_branch(self, response):
        item = ZooplaItem()
        item["Name"] = response.xpath(
            '//div[contains(@class,"sidebar")]//*[@itemprop="name"]/text()').extract_first(default='').strip()

        address_list = response.xpath(
            '//div[contains(@class,"sidebar")]//*[@itemprop="address"]/text()').extract_first(default='').split(',')
        item["Zipcode"] = address_list[-1].strip()
        if len(address_list) > 2:
            item["Locality"] = address_list[-2].strip()
            item["Street"] = ', '.join([i.strip() for i in address_list[:-2]]).strip()
        else:
            item["Locality"] = ''
            item["Street"] = ', '.join([i.strip() for i in address_list[:-1]]).strip()

        item["Phone"] = response.xpath(
            '//div[contains(@class,"sidebar")]//*[@itemprop="telephone"]/text()').extract_first(default='').strip()

        if item["Phone"] and item["Phone"][:3] == '020':
            item["Phone"] = '+44 ' + item["Phone"][1:]

        item["Website"] = response.xpath(
            '//div[contains(@class,"sidebar")]//a[contains(text(),"website")]/@href').extract_first(default='')

        yield item
