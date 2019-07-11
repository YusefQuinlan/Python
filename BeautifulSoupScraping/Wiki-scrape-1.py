
"""
Created on Mon Jun 24 16:38:29 2019

@author: Yusef Quinlan
"""

from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/Kim_Seok-jin')
soup = BeautifulSoup(r.text, 'html.parser')



records = []
ContentsBox = soup.find('div', class_='toc')

#The craper does not work to full capacity as it prints out â€“  instead of the -
#Character, this is a problem of utf-8 that I must try and solve.
List_items = ContentsBox.findAll('li')
for i in List_items:
    Content_no = i.find('span').text
    Content = i.find('span', class_='toctext').text.replace('â€“', "-")
    records.append((Content_no, Content))
    
import pandas as pd

DataFrameM8 = pd.DataFrame(records, columns=['Content_numero','Contenido'])

DataFrameM8.to_csv('Random_wiki_page1.csv', index= False, encoding = 'utf-8')
