# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewSpider(scrapy.Spider):
    name = "amazon_review"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'http://www.amazon.com/',
    )

    def parse(self, response):
        pass
