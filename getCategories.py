# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 04:53:57 2022

@author: Pikachu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
from getPageCount import get_categories_all_pages

url = "https://www.4cmusic.com"

print("baslanbgıc")

#page = urlopen(url)
#html = page.read().decode("latin-1")
#start_index = html.find("<header>") + len("<header>")
#end_index = html.find("</header>")
#title = html[start_index:end_index]


page = requests.get(url)
page = page.content
#soup = BeautifulSoup(page "html.parser")
soup = BeautifulSoup(page.decode('utf-8','ignore'))
#results = soup.find(id="cat_accordion")
categories = soup.select("ul#cat_accordion>li>ul>li>a")
print(categories)
allCategories = []
for i in categories:
    time.sleep(3)
    print("link" + i["href"])
    #get_categories_all_pages(i["href"])
"""for i in categories:
    #neo = i.find_parent("li")
    neo = i
    if(len(neo)):
        neo= neo[0].select("li > a", recursive=False)
        for j in neo:
            if(len(j)):
                
                print("HEY -- ", j)
            #allCategories.append(neo)
"""
count = 1
for j in allCategories:
    try:
        #print(j)
        count+=1
    except():
        print("error")