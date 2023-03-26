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
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.error import HTTPError

url = "https://www.4cmusic.com/products/Davul"
#options to add as arguments
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument("start-maximized"); # open Browser in maximized mode
options.add_argument("disable-infobars"); # disabling infobars
options.add_argument("--disable-extensions"); # disabling extensions
options.add_argument("--disable-gpu"); # applicable to windows os only
options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox"); # Bypass OS security model
options.add_argument('--headless')
#chrome to stay open
options.add_experimental_option("detach", True)

def get_all_product_pages(url, dic_child, j):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    print(url)
    try:
        page = urlopen(url)
    except HTTPError as e:
        content = e.read()
        print("HTTP error encountered while reading URL" + url)
    soup = BeautifulSoup(page, "html.parser")

    results = soup.find("div", class_="product-grid")
    results = results.find_all("div", class_="grid_box")
   
    for i in results:
        dictionary = {}
        result = i.find("a")
        result = result["href"]
        try:
            page = urlopen(result)
        except HTTPError as e:
            content = e.read()
            print("HTTP error encountered while reading URL")
        soup = BeautifulSoup(page, "html.parser")

        browser.get(result)
        time.sleep(2)
        
        try:
            product_title = browser.find_element(
                "xpath", "/html/body/div[2]/div/div[1]/div[2]/h2").text

            product_description = soup.find(id="tab-description")
            photo_link = browser.find_element(
                "xpath", "/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/a[1]").get_attribute('href')
            price = browser.find_element("xpath", "/html/body/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[3]/span[1]").get_attribute('innerText')
            dictionary = {
                'title': str(product_title),
                'description': str(product_description),
                'photo_url': str(photo_link),
                'price': price,
                'id': str(j)
            }
        except:
            print("Photo exception\n")
        
        dic_child.append(dictionary)
        j+=1
        time.sleep(3)
    print(dic_child)

    return j, dic_child.copy()