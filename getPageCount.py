# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 06:45:24 2022

@author: Pikachu
"""
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
from getProducts import get_all_product_pages 
#url = "https://www.4cmusic.com/products/gitar"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_categories_all_pages(url = "https://www.4cmusic.com/products/gitar"):
    page = urlopen(str(url))
    soup = BeautifulSoup(page, "html.parser")
    categories = soup.select("ul#cat_accordion>li>ul")
    item = categories[0].select("li>a")
    ens_type = url.split("/")[-1] #.partition("?")[0]
    outfile = open("./"+ ens_type + ".json", "a+")
    print("ens_type " +ens_type)
    for it in item:
        
        page = urlopen(it["href"])
        ens_type = it["href"].split("/")[-1] #.partition("?")[0]
        outfile = open("./"+ ens_type + ".json", "a+")
        soup = BeautifulSoup(page, "html.parser")
        results = soup.find(string=">|")
        
        print(results)
        flag=0
        
        dic_parent = {}
        j=0
        dic_child=[]
        url = it["href"]
        ens_type = url.split("/")[-1]
        print(url)
        print(ens_type)
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
                
        print(results)
        if(flag):
            page = []
            j, dic_child = get_all_product_pages(url, dic_child,j)
                                  
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
                j, dic_child = get_all_product_pages(url+"?&page="+str(i), dic_child,j)
        dic_parent[ens_type] = dic_child
        json_data = json.dumps(dic_parent)
        outfile.write(json_data)
