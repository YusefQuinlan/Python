# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:31:38 2019

@author: Yusef Quinlan
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
Currency_Names = []
Currency_Links = []
Currency_prices= []



#this hasnt worked, we need to find the way to get the actual Html from the href
def GetLinksNames(Names) :
    Requested = requests.get('https://coinmarketcap.com/coins/')
    Soup = BeautifulSoup(Requested.text, "html.parser")
    for i in Soup.findAll('a', class_='currency-name-container link-secondary'):
        print(i['href'].split('/')[2])
        Names.append(i['href'].split('/')[2])
        
   

def GetCurrencyprices(price_list):
    Requested = requests.get('https://coinmarketcap.com/coins/')
    Soup = BeautifulSoup(Requested.text, "html.parser")
    for i in Soup.findAll('a', class_='price'):
        print(i.text)
        price_list.append(i.text)
        
        

    
GetLinksNames(Currency_Names)
GetCurrencyprices(Currency_prices)
#THIS IS TO BE CONTINUED, SUGGESTIONS ARE SELENIUM(PYTHON MODULE/PACKAGE) 
#THE OTHER SUGGESTION IS TO USE JAVASCRIPT BECAUSE A PARSER DOESN'T READ HTML
#APPARENTLY BEAUTIFUL SOUP CANNOT GET THE HTML FROM THE HREF
#THIS MUST BE SOLVED AT A LATER DATE BUT IS A NICE DISPLAY OF PYTHON FOR NOW.
#RESOLVED THE PROBLEM NOW BUT IN A DIFFERENT WAY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
csv_file = open('Cryptos.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(Currency_Names)
csv_writer.writerow(Currency_prices)
csv_file.close()

with open('Cryptos.csv', 'a') as fd:
    Currency_prices2 = []
    GetCurrencyprices(Currency_prices2)
    writer = csv.writer(fd)
    writer.writerow(Currency_prices2)