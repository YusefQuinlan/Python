# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:27:25 2019

@author: Yusef Quinlan
"""

    from bs4 import BeautifulSoup
    import requests
    
    r = requests.get('https://www.hipforums.com/forum/threads/far-right-attacks-on-pride-celebrations.494111/#post-8482064')
    soup = BeautifulSoup(r.text, 'html.parser')
    UserTexts = soup.findAll('h3', class_='userText')
    UserComments = soup.findAll('div', class_='messageContent')
    
    Usernames = []
    Comments = [] 
    UserAll = []
    name = 'l'
    comment = 's'
    count = 0
    count2 = 0
    for i in range(0, len(UserTexts)):
        print(UserTexts[i])
        Usernames.append(UserTexts[i].a.text)
     
    for i in range(0, len(UserComments)):
        print(UserComments[i])
        Comments.append(UserComments[i].text.replace("\n\t\t\t\t\n\t\t\t\t\t↑\n\n"," ").replace(\
                        "\n\t\t\t\t\t\xa0\n\n\n", " ").replace("\n\n\n\n\n", " ")\
        .replace("\n\n\n\t\t\t\t\t\n\t\t\t\t\t"," ").replace("\n"," ").replace("\n\n", " ")\
        .replace("\n\n\n\xa0\n\n\n", " ").replace("\xa0", " "))
    
    
    
    for i in range(0, len(UserComments) * 2):
        
        if count2 % 2 == 0:
            name = Usernames[i - count]
            count = count+1
            count2 = count2 + 1
        else:
            comment = Comments[i - count]
            UserAll.append((name,comment))
            count2 = count2 + 1