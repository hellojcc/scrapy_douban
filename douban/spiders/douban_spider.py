# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list=response.xpath("//*[@id=\"content\"]/div/div[1]/ol/li")
        for i_item in movie_list:
            douban_item=DoubanItem()
            douban_item['serial_number']=i_item.xpath("./div/div[1]/em/text()").extract_first()
            douban_item['movie_name']=i_item.xpath("./div/div[2]/div[1]/a/span[1]/text()").extract_first()
            content=i_item.xpath("./div/div[2]/div[2]/p[1]/text()").extract() #没有first
            for i_content in content:
                content_s="".join(i_content.split())
                douban_item["introduce"]=content_s
            douban_item['star']=i_item.xpath("./div/div[2]/div[2]/div/span[2]/text()").extract_first()
            douban_item['evaluate']=i_item.xpath("./div/div[2]/div[2]/div/span[4]/text()").extract_first()
            douban_item['describe']=i_item.xpath("./div/div[2]/div[2]/p[2]/span/text()").extract_first()
            yield douban_item
            #print(douban_item)
        next_link=response.xpath("//*[@id=\"content\"]/div/div[1]/div[2]/span[3]/a/@href").extract()
        print(next_link)
        if next_link:
            next_link=next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
