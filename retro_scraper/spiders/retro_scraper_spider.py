# Implementation of scrapy to scrape information about classic games on retrogamer website.

import scrapy

# Importing modules to allow debbuging the spider like any other pthon script.
# from scrapy.crawler import CrawlerProcess

class RetroSpider(scrapy.Spider):
	name = "retrogames"
	start_urls = ['https://www.retrogamer.net/']

	def parse(self, response):
		for blog in response.css('article'):
			blog_tag = blog.css('a.CatBadge.blog_post').get()
			if blog_tag is not None:
				blog_article = blog.css('a.thumbLink::attr(href)').get()
				yield response.follow(blog_article, callback = self.parse_blog)

	def parse_blog(self, response):
		content = response.css('div.entry-content')
		yield {
			'title': response.css('h1.entry-title::text').get(),
			'text': content.css('p::text').getall(),
		}

# Bellow we call the functions to turn possible debuging it using break points
# process = CrawlerProcess()
# process.crawl(RetroSpider) # Must call the spider by its class name, not the attribute name
# process.start() # Execute the above spider as normal python script
