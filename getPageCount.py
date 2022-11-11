# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 06:45:24 2022

@author: Pikachu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
from getProducts import get_all_product_pages 
#url = "https://www.4cmusic.com/products/gitar"


def get_categories_all_pages(url):
    
   
    page = urlopen(str(url))
    
    soup = BeautifulSoup(page, "html.parser")
    results = soup.find(string=">|")
    print(url)
    flag=0
    if(results):
        results=(results.find_parent())
    else:
        results=soup.find("div",class_="pagination")
        try:
            results = results.find("div",class_="links")
            results = results.find_all("a")
            lenOf = len(results)-2
            
            results = results[lenOf]
            print(results)
        except:
            flag = 1
            
    
        
        
    
    if(flag):
        page = []
        get_all_product_pages(url)
                              
    else:
        lenOf=len(results["href"])
    
        page = str(results["href"][lenOf-2]) + str(results["href"][lenOf-1])
    
    
        if(page[0]=="="):
            page = str(results["href"][lenOf-1])
            print(page)
        else:
            print("çift hane")
            
        print(page)
        
        for i in range(1,int(page)+1):
            get_all_product_pages(url+"?&page="+str(i))  