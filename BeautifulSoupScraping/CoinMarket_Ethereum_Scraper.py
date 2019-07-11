# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:59:54 2019

@author: Yusef Quinlan
"""

from bs4 import BeautifulSoup
import requests

requested = requests.get('https://coinmarketcap.com/currencies/ethereum/')
Soup = BeautifulSoup(requested.text, "html.parser")
gertrude = Soup.findAll('span', class_='h2 text-semi-bold details-panel-item--price__value')
Current_Price = gertrude.text
print(Current_Price)

Heavy = 'https://coinmarketcap.com/currencies/ethereum/'
Heavy2 = Heavy.split('/')
Currency_name = Heavy2[4]

