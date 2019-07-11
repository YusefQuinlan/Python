# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:24:20 2019

@author: Yusef_Quinlan
"""

from bs4 import BeautifulSoup
import requests
count = 0
list_pages = []
for i in range(0,10):
    if count != 1:
        list_pages.append('http://boards.4channel.org/biz/simbad'.replace('simbad', str(count)))
        count = count + 1
    if count == 1:
        count = count + 1
this = 'http://boards.4channel.org/biz/'
r = requests.get(this)
soup = BeautifulSoup(r.text, 'html.parser')

for i in list_pages:
    r = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.find('a'))

for i in soup.findAll('a'): 
    if i.text.isdigit():
        if int(i.text) < 11:
            
        
            print(i.text)
            print('lol')