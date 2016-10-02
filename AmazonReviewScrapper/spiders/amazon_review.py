# -*- coding: utf-8 -*-
import scrapy
import csv
from AmazonReviewScrapper.items import ReviewsItem

with open('amazonreviewpages.txt', 'rU') as file:
    rows = csv.reader(file)
    urls = []
    for row in rows:
        urls.append(row)


class AmazonReviewSpider(scrapy.Spider):
    name = "amazon_review"
    download_delay = 10
    allowed_domains = ["amazon.com"]
    # start_urls = (
    #     'https://www.amazon.com/Muse-Brain-Sensing-Headband-Black/product-reviews/B00LOQR37C',
    # )
    # start_urls = list(urls)
    def start_requests(self):
        urls = []
        with open('amazonreviewpages.txt', 'rU') as file:
            rows = csv.reader(file)
            for row in rows:
                urls.append(row[0])
        # urls = [
        #     'https://www.amazon.com/Muse-Brain-Sensing-Headband-Black/product-reviews/B00LOQR37C/ref=cm_cr_arp_d_paging_btm_1?ie=UTF8&pageNumber=1',
        #     'https://www.amazon.com/Muse-Brain-Sensing-Headband-Black/product-reviews/B00LOQR37C/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&pageNumber=2',
        # ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        for itemid in response.xpath('//*[@class="a-section review"]'):
            reviewitem = ReviewsItem()

            reviewid = itemid.xpath('@id').extract()[0]
            reviewTitle = response.xpath('//*[@id="%s"]/div[1]/a[2]/text()' %reviewid).extract()[0]
            reviewRate = response.xpath('//*[@id="%s"]/div[1]/a[1]/i/span/text()' %reviewid).extract()[0]
            reviewer = response.xpath('//*[@id="%s"]/div[2]/span[1]/a/text()' %reviewid).extract()[0]
            reviewDate = response.xpath('//*[@id="%s"]/div[2]/span[4]/text()' %reviewid).extract()[0]
            review = (',').join(response.xpath('//*[@id="%s"]/div[4]/span/text()' %reviewid).extract())

            reviewitem['reviewid'] = reviewid
            reviewitem['reviewTitle'] = reviewTitle
            reviewitem['reviewRate'] = reviewRate
            reviewitem['reviewer'] = reviewer
            reviewitem['reviewDate'] = reviewDate
            reviewitem['review'] = review

            yield reviewitem

        pass
