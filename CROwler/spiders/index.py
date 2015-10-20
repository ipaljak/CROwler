# -*- coding: utf-8 -*-

from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from re import match

from CROwler.items import Comment

class IndexSpider(CrawlSpider):
    
    name = "index"
    allowed_domains = ["index.hr"]
    start_urls = ['http://www.index.hr/indexforum/postovi/222640/karamarko-treba-nam-vojska-na-granici-postat-cemo-humanitarni-problem-europe/1']

    rules = [
            Rule(LinkExtractor(restrict_xpaths=('//div[@class="topPager"]/ul/li/a')), 
                 callback='parse_item', 
                 follow=True), 

            ]

    def parse_item(self, response):
        sel = Selector(response)
        comments = sel.xpath('//div[@class="inner"]')
        items = [] 

        for comment in comments[:-1]:
            
            item = Comment()
            
            item['user']        = comment.xpath('.//div[@class="colL"]//a[@class="user"]/@title').extract()
            item['user_rating'] = comment.xpath('.//div[@class="rateit"]/@data-rateit-value').extract()
            item['post_count']  = comment.xpath('.//div[@class="colL"]//div/span/text()').re('.*?(\d+)$')

            item['text']        = comment.xpath('.//div[@class="postText"]/p//text()').extract()
            item['thumbs']      = comment.xpath('../div[@class="postActions"]/a/span/text()').extract()  
            item['quotes_user'] = comment.xpath('.//div[@class="colR"]//span/a/text()').extract()
            item['quoted_text'] = comment.xpath('.//div[@class="postText"]/blockquote//text()').extract() 

            items.append(item)

        return items

