# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:44:34 2019

@author: Yusef Quinlan
"""
#This scraper is more or less successful at this point, I didnt work out the next button but found an alternative
#The alternative only works because I know how many pages there are, it will not work when I dont know
#I need to find a way to use the text of an a tag as a reference point to get a href from.
import scrapy

class BigSpider(scrapy.Spider):
    name = 'FunScraper2'
    start_urls = [
               'https://coinmarketcap.com/'          
            ]

    def parse(self, response):
        all_links = response.css('td.no-wrap.currency-name')
        count = 0
        for i in all_links:
            links2 = 'https://coinmarketcap.com' + i.css('a.currency-name-container ::attr(href)').get()
            link_text = i.css('a.currency-name-container::text').extract()
            links3 = i.css('a.currency-name-container ::attr(href)').get() + '#markets'
            simber = response.css('td.no-wrap.text-right a.price::text').extract()[count]
            
            
            count = count + 1
            
            yield { 'Links2':links2, 'text':link_text, 'dollar_value':simber}
        print('the response is:  ' + str(response))
        number = 1
        if str(response) == '<200 https://coinmarketcap.com/>':
            number = 2
        if str(response) != '<200 https://coinmarketcap.com/>':
            numba = str(response).replace('<200 https://coinmarketcap.com/', '' ).replace('>','')
            number = int(numba) + 1
        print('number issssss:  ' + str(number))
        if number <= 23:
            
            next_page = 'https://coinmarketcap.com/' + str(number)
            print(next_page)
            yield response.follow(next_page, callback = self.parse)
       
            