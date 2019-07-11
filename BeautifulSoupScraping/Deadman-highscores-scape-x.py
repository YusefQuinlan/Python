#here I am making a program that grabs data from several pages in a website that has the same page name + 1 per each webpage i.e
# Webpage1.com, webpage2.com, Webpage3.com up to for example Webpage9001.com and showing how to add each page to the list using a loop,
# Rather than having to add every page to the list manually.

#import requests and beautiful soup
from bs4 import BeautifulSoup
import requests
#make empty list of webpages
list_of_dmm_pages = []
#make Secondary list so we can get a list length and use it as our webpage number
pagenod = ['1']

#Append each item to the secondary list by 1 per item to increase list length and use list length and replace to change website number for pages in range
for items in range(0, 69):
    list_of_dmm_pages.append('http://services.runescape.com/m=hiscore_oldschool_deadman/overall.ws?table=0&page=simba'.replace('simba', str(len(pagenod))))
    pagenod.append('1')


#make the blank list to put data into in the end
List_of_highscores = []
for item in list_of_dmm_pages:
    r = requests.get(item)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all('tr' , attrs={'class':'personal-hiscores__row'})
#add to the highscores list of every webpage
    for information in results:
        Rank = information.contents[1].text[1:-1]
        Name = information.contents[3].text[1:-1].replace("\xa0", " ")
        Level = information.contents[5].text[1:-1]
        xp = information.contents[7].text[1:-1]
        List_of_highscores.append((Rank, Name, Level, xp))

import pandas as pd
df = pd.DataFrame(List_of_highscores, columns=['Rank', 'Name', 'Total_level', 'Total_xp'])

df.to_csv('Deadman-Highscores-table-70-pages.csv', index=False, encoding='utf8')
