# -*- coding: utf-8 -*-
import scrapy
import requests
import sys

num=0
def download_pic(url):
    img = requests.get(url,allow_redirects=True).content
    global num
    img_name ='{0}.jpg'.format(str(num))
    num = num+1
    open(img_name,'wb').write(img)

class QuotesSpider(scrapy.Spider):
    name = 'quote'
    # allowed_domains = ['twitter.com']
    # start_urls = ['{1}'].format(str(sys.argv[1]))
    start_urls = ['https://www.google.ca/search?biw=1440&bih=803&tbm=isch&sa=1&ei=pAKaWrOgN4WPjwS4w4_oCw&q=%E7%BE%8E%E5%A5%B3&oq=%E7%BE%8E%E5%A5%B3&gs_l=psy-ab.3...1953.10647.0.10768.18.11.7.0.0.0.94.625.8.10.0....0...1c.1j4.64.psy-ab..1.13.485.0..0j0i67k1j0i30k1j0i5i30k1j0i24k1.114.zqSN5x3bvVE']

    def parse(self, response):
        list_of_pic = response.css('img::attr(src)').extract()
        for u in list_of_pic:
            print(u)
            download_pic(u)
            if num >20:
                exit()
