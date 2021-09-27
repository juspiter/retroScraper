# Implementation of scrapy to scrape information about classic games on retrogamer website.

import scrapy

# Importing modules to allow debbuging the spider like any other pthon script.
from scrapy.crawler import CrawlerProcess

class RetroSpider(scrapy.Spider):
	name = "retrogames"
	start_urls = ['https://www.retrogamer.net/']

	def parse(self, response):
		for blog in response.css('article').getall():
			blog_tag = blog.css('a.CatBadge blog_post').get()
			if blog_tag is not None:
				blog_article = blog.css('a.thumbLink a::attr(href)').get()
				yield response.follow(blog_article, callback=self.parse)

# Bellow we call the functions to turn possible debuging it using break points
process = CrawlerProcess()
process.crawl(RetroSpider) # Must call the spider by its class name, not the attribute name
process.start() # Execute the above spider as normal python script
