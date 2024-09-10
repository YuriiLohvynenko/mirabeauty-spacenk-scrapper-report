import re
import csv
import requests
# import numpy as np
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
# page = requests.get('https://mirabeauty.com/aesop/parsley-seed-anti-oxidant-serum')
# soup = BeautifulSoup(page.content,"html.parser")
# brand = soup.find('span', attrs={'class':'brand'}).text
driver = webdriver.Chrome(executable_path='E:/scrapping_jack/Mirabeauty/chromedriver')
driver.get('https://mirabeauty.com/aesop/parsley-seed-anti-oxidant-serum')
time.sleep(3)
pricebutton = driver.find_element_by_class_name('price-btn')
pricebutton.click()
time.sleep(2)
# print(driver.find_element_by_class_name('fulfillment-attribution'))
# print(driver.find_element_by_class_name('fulfillment-attribution').text)
soup = BeautifulSoup(driver.page_source,"html.parser")
print(soup.find('div',attrs={'class':'fulfillment-attribution'}).text)
driver.close()