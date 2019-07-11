#This is the lottery data scraper so I can make a lottery number predicting NN
#Just scraping 1 page

#Import requests and BeautifulSoup
from bs4 import BeautifulSoup
import requests

#Source data collect and parse with Soup
r = requests.get("http://lottery.merseyworld.com/cgi-bin/lottery?days=20&Machine=Z&Ballset=0&order=1&show=1&year=0&display=NoTables")
soup = BeautifulSoup(r.text, "html.parser")
#Create a text file and then extract info from the text file
file = open("Euro_millions_data.txt","w")
file.write(soup.text[135:-1225])
#this text file will be used in a different program
#the other program will extract this data and I will implement
#Some form of probability algorithm for the numbers
#I will try and make it a Neural net that can guess the most likely
#combination of numbers and 1000 examples of win predictions
#I will test the big prediction and 9 of the 1000 examples
#this will allow me to see how accurate my program is
#the lottery sample size might be too small.
