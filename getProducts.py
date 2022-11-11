# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:07:36 2022

@author: Pikachu
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import json

browser = webdriver.Chrome(executable_path=r"C:\Users\Pikachu\Desktop\Sülale\The Musicians\chromedriver.exe")
url = "https://www.4cmusic.com/products/Davul"


def get_all_product_pages(url):

    outfile = open("sample.json", "w")
    page = urlopen(url)
    
    soup = BeautifulSoup(page, "html.parser")
    
    results = soup.find("div", class_="product-grid")
    results= results.find_all("div", class_="grid_box")
    
    
    for i in results:
        result =i.find("a")
        result = result["href"]
        page = urlopen(result)
        
        soup = BeautifulSoup(page, "html.parser")
        browser.get(result)
        time.sleep(3)
        product_title = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/h2").text
      
        product_description = soup.find(id= "tab-description")
        try:
            photo_link =browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/a[1]").get_attribute('href')
            print(product_title)
        except:
            print("Photo exception\n")
        dictionary = {
            'title' : str(product_title),
            'description': str(product_description),
            'photo_url': str(photo_link)
        }
        json_data = json.dumps(dictionary)
        
        outfile.write(json_data)
        time.sleep(2)   
    
