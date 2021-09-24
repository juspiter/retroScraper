# Implementation of scrapy to scrape information about classic games on retrogamer website.

import scrapy

class RetroSpider(scrapy.Spider):
	name = "retrogames"
	start_urls = ['https://www.retrogamer.net/']

	def parse(self, response):
		for blog in response.css('article').getall():
			blog_tag = blog.css('a.CatBadge blog_post').get()
			if blog_tag is not None:
				blog_article = blog.css('a.thumbLink a::attr(href)').get()
				yield response.follow(blog_article, callback=self.parse)