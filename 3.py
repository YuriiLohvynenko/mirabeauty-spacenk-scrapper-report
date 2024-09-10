'''571Gustavus_Adolphus_College'''
import re
import csv
import requests
# import numpy as np
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql



def textskin(text):
    return text.replace("'","@@@").replace('"','###')
    

def product_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    brand = soup.find('span', attrs={'class':'brand'}).text
    print('brand: '+brand)
    product = soup.find('h1').text
    print('product: '+product)
    category_temp = soup.find_all('a', attrs={'class':'link'})
    category = category_temp[1].text
    print('category: ' + category)
    try:
        price = soup.find('span', attrs={'class':'price'}).text
    except:
        price=''
    print('price: '+price)
    try:
        rating = soup.find('span', attrs={'class':'rating'})
        real_rating = rating.find('span').text
    except:
        real_rating = ''
    
    print('rating: '+real_rating)
    try:
        review = soup.find('span', attrs={'class':'review'})
        real_review = review.find('span').text.replace("(",'').replace(")",'').replace('"','')
    except:
        real_review = '0'
    
    print('review: '+real_review)
    
    # buttontemp = soup.find('span', attrs={'class':'item'})
    try:
        viewon_first = soup.find('span', attrs={'class':'seller'}).text
    except:
        viewon_first = ''
    
    print('viewon_first: '+viewon_first)
    # try:
    #     viewon_link = soup.find('a', attrs={'class':'price-btn'}).get('href')
    # except:
    #     viewon_link = ''

    
    
    try:
        viewon_link_title = soup.find('a', attrs={'class':'price-btn'}).text
        

    except:
        viewon_link_title = ''
    print('viewon_link_title: '+viewon_link_title)


    fullfilledby = ''
    if viewon_link_title == '':
        checkout = ''
        viewon_link = ''
        button_statue = '0'
    elif viewon_link_title == 'Add to Cart':
        checkout = 'Add to Cart'
        viewon_link = ''
        driver = webdriver.Chrome(executable_path='E:/scrapping_jack/Mirabeauty/chromedriver')
        driver.get(url)
        time.sleep(4)
        pricebutton = driver.find_element_by_class_name('price-btn')
        pricebutton.click()
        time.sleep(4)
        soup1 = BeautifulSoup(driver.page_source,"html.parser")
        
        try:
            fullfilledby = soup1.find('div',attrs={'class':'fulfillment-attribution'}).text
            fullfilledby = fullfilledby.replace('Fulfilled by ', '')
        except:
            fullfilledby = ''
        # print(soup1.find('div',attrs={'class':'fulfillment-attribution'}).text)
        driver.close()
        button_statue = '1'
    else:
        checkout = 'Link' 
        viewon_link = soup.find('a', attrs={'class':'price-btn'}).get('href')
        button_statue = '2'
    print('viewon_link: '+viewon_link)
    print('checkout: ' + checkout)
    print('fullfilledby: ' + fullfilledby)
    try:
        alternative_retailers_temp = soup.find('div', attrs={'class':'mira-more-sellers item center-item'})
        alternative_retailers_first = alternative_retailers_temp.find('a').text
        alternative_retailers_link = alternative_retailers_temp.find('a').get('href')
        button_statue = '3'
    except:
        alternative_retailers_first = ''
        alternative_retailers_link = ''
    print('alternative_retailers_first: ' + alternative_retailers_first)
    print('alternative_retailers_link: ' + alternative_retailers_link)
    try:
        review_websites_temp = soup.find_all('span', attrs={'class':'display-name'})
        review_websites = ''
        for i in range(len(review_websites_temp)):
            if review_websites == '':
                review_websites = review_websites_temp[i].text.replace(' user','')
            else:
                if review_websites_temp[i].text.replace(' user','') in review_websites:
                    review_websites = review_websites
                else:
                    review_websites = review_websites + ', ' + review_websites_temp[i].text.replace(' user','')
    except:
        review_websites = ''
    # review_websites = textskin(review_websites)
    print('review_websites: ' + review_websites)
    

    brand = textskin(brand)
    category = textskin(category)
    product = textskin(product)
    
    real_review = int(real_review)
    
    viewon_first = textskin(viewon_first)
    viewon_link = textskin(viewon_link)
    fullfilledby = textskin(fullfilledby)
    alternative_retailers_first = textskin(alternative_retailers_first)
    alternative_retailers_link = textskin(alternative_retailers_link)
    review_websites = textskin(review_websites)
    url = textskin(url)

    # sql = "INSERT INTO listing (name, address) VALUES (%s, %s)"
    sql = "INSERT INTO `listing`(`brand`, `category`, `product`, `price`, `rating`, `review`, `viewon_first`, `viewon_link`, `checkout`, `fullfilledby`, `alternative_retailers_first`, `alternative_retailers_link`, `review_websites`, `button_statue`, `product_url`) VALUES ('%s','%s','%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (brand, category, product, price, real_rating, real_review, viewon_first, viewon_link, checkout, fullfilledby, alternative_retailers_first, alternative_retailers_link, review_websites, button_statue, url)
    # val = (brand, category, product, price, real_rating, real_review, viewon_first, viewon_link, checkout, fullfilledby, alternative_retailers_first, alternative_retailers_link, review_websites, button_statue)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

def extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    data = soup.find('div',attrs={'class':'mira-pagination'})
    # print(data)
    try:
        pagenumber_temp = data.find_all('a')
        # print(pagenumber_temp)
        pagenumber = pagenumber_temp[len(pagenumber_temp)-2].text
    except:
        pagenumber = data.find('a').text

    print('pagenumber: '+pagenumber)
    for i in range(int(pagenumber)):
        page_url = url + '?page=' + str(i+1)
        print(page_url)
        page1 = requests.get(page_url)
        soup1 = BeautifulSoup(page1.content,"html.parser")
        product_data = soup1.find_all('a', attrs={'class':'card-inner-container'})
        for i in range(len(product_data)):
            product_url = 'https://mirabeauty.com' + product_data[i].get('href')
            print(product_url)
            sql = "SELECT `product_url` FROM `listing` WHERE `product_url`='%s'" % (product_url)
            try:
                # Execute the SQL command
                # cursor.execute(sql)
            
                
                cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                # rows = cursor.fetchmany(size=1)
                results = cursor.fetchall()
                row_counts = len(results)
                
                if row_counts > 0:
                    print('existing')
                else:
                    product_info(product_url)
            except:
                print ("Error: unable to fetch data")
             
        # product_info('https://mirabeauty.com/bh-cosmetics/take-me-back-to-brazil-eyeshadow-palette')
        

    # a = data.find_all('a')
    
    # print(a[len(a)].text)
# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

durl = 'https://mirabeauty.com/'
# page = requests.get(durl)
# soup = BeautifulSoup(page.content,"html.parser")
driver = webdriver.Chrome(executable_path='E:/scrapping_jack/Mirabeauty/chromedriver')
driver.get(durl)
time.sleep(4)
soup = BeautifulSoup(driver.page_source,"html.parser")
data3 = soup.find_all('div',attrs={'class':'subcategories-container'})
aurl = data3[3].find_all('a')
for i in range(7,len(aurl)):


    if aurl[i].get('href') != '#':
        url='https://mirabeauty.com'+ aurl[i].get('href')
        extract(url)
        
        # print(url)
# disconnect from server
db.close()



