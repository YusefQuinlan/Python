# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:44:13 2019

@author: Yusef Quinlan
"""
#This is a fully working scraper for coinmarket.com made with scrapy frameworks
#it is able to extract information such as the name of the currency, the value of the currency
#in USD and the link to the currency page, this could be output in a csv or json file etc
#the info is scraped from the coinmarket front page and scrapes the top 100 cryptos from that page.
import scrapy

class BigSpider(scrapy.Spider):
    name = 'FunScraper'
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