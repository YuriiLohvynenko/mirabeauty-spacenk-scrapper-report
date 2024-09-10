import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql
import time
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date 

def textskin(text):
    return text.replace("'","@@@").replace('"','###')

def get_data(soup, driver, brand, product, category, product_url):
    try:
        
        data = soup.find('div', attrs={'class':'bv-content-list-container'})
        rowdata = data.find_all('li', attrs={'class':'bv-content-item bv-content-top-review bv-content-review'})
        for j in range(len(rowdata)):
            # userdata = rowdata.find('div', attrs={'class':'bv-author-profile'})
            username = rowdata[j].find('div', attrs={'class':'bv-content-author-name'}).text
            reviews = rowdata[j].find('span', attrs={'class':'bv-author-userstats-value'}).text
            location = rowdata[j].find('div', attrs={'class':'bv-author-location'}).text
            print('username: ' + username)
            print('reviews: ' + reviews)
            print('location: ' + location)
            userinfo_data = rowdata[j].find_all('span', attrs={'class':'bv-author-userinfo-data'})
            userinfo_value = rowdata[j].find_all('span', attrs={'class':'bv-author-userinfo-value'})
            for i in range(len(userinfo_data)):
                # print(userinfo_data[i])
                if userinfo_data[i].text == 'Age':
                    age = userinfo_value[i].text
                    print('age: '+age)
                elif userinfo_data[i].text == 'Gender':
                    gender = userinfo_value[i].text
                    print('gender: '+gender)
                elif userinfo_data[i].text == 'Skin Type:':
                    skin_type = userinfo_value[i].text
                    print('skin_type: '+skin_type)
                elif userinfo_data[i].text == 'What is your hair length?':
                    hair_length = userinfo_value[i].text
                    print('hair_length: '+hair_length)
                elif userinfo_data[i].text == 'What is your hair colour?':
                    hair_color = userinfo_value[i].text
                    print('hair_color: '+hair_color)
                elif userinfo_data[i].text == 'What is your hair goal?':
                    hair_goal = userinfo_value[i].text
                    print('hair_goal: ' + hair_goal)
                elif userinfo_data[i].text == 'Skin Tone:':
                    skin_tone =  userinfo_value[i].text
                    print('skin_tone: '+skin_tone)
                elif userinfo_data[i].text == 'Hair Type:':
                    hair_type = userinfo_value[i].text
                    print('hair_type: ' + hair_type)
                elif userinfo_data[i].text == 'Skincare Concern:':
                    skincare_concern = userinfo_value[i].text
                    print('skincare_concern: '+skincare_concern)
            try:
                review_date = rowdata[j].find('span', attrs={'class':'bv-content-datetime-stamp'}).text
            except:
                review_date = ''
            print('review_date: ' + review_date)
            try:
                review_rating = rowdata[j].find('span', attrs={'class':'bv-off-screen'}).text
                review_rating_array = review_rating.split()
                review_rating = review_rating_array[0]
            except:
                review_rating = ''
            print('review_rating: '+review_rating)
            try:
                bestuse_temp = rowdata[j].find_all('li', attrs={'class':'bv-content-data-value'})
                bestuse = ''
                for i in range(len(bestuse_temp)):
                    bestuse = bestuse + bestuse_temp[i].text
            except:
                bestuse = ''
            print('bestuse: ' + bestuse)
            try:
                recommend_product = rowdata[j].find_all('span', attrs={'class':'bv-content-data-label'})
                recommend_product = recommend_product[1].text
            except:
                recommend_product = ''
            print('recommend_product: '+recommend_product)
            try:
                review_title = rowdata[j].find('h3', attrs={'class':'bv-content-title'}).text
            except:
                review_title = ''
            print('review_title: ' + review_title)
            try:
                review_content = rowdata[j].find('div', attrs={'class':'bv-content-summary-body-text'}).text
            except:
                review_content = ''
            print('review_content: ' + review_content)
            currentday = date.today()
            print("current_day: " + str(currentday))
            currentday = str(currentday)
            username = textskin(username)
            location = textskin(location)
            age = textskin(age)
            gender = textskin(gender)
            skin_type = textskin(skin_type)
            hair_length = textskin(hair_length)
            hair_color = textskin(hair_color)
            hair_goal = textskin(hair_goal)
            skin_tone = textskin(skin_tone)
            hair_type = textskin(hair_type)
            review_date = textskin(review_date)
            bestuse = textskin(bestuse)
            recommend_product = textskin(recommend_product)
            review_title = textskin(review_title)
            review_content = textskin(review_content)
            userinfo_insert_sql = "INSERT INTO `spacenk_user`(`username`, `reviews`, `location`, `age`, `gender`, `skin_type`, `hair_length`, `hair_color`, `hair_goal`, `skin_tone`, `hair_type`, `skincare_concern`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (username, reviews, location, age, gender, skin_type, hair_length, hair_color, hair_goal, skin_tone, hair_type, skincare_concern)
            try:
                # Execute the SQL command
                cursor.execute(userinfo_insert_sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
            # sql = "SELECT * FROM `spacenk_user` WHERE `username`='%s'" % (username)
            # try:
            #     # Execute the SQL command
            #     # cursor.execute(sql)
            
                
            #     cursor.execute(sql)
            #     # Fetch all the rows in a list of lists.
            #     # rows = cursor.fetchmany(size=1)
            #     results = cursor.fetchall()
            #     row_counts = len(results)
                
            #     if row_counts > 0:
            #         print('user already existed')
            #     else:
            #         userinfo_insert_sql = "INSERT INTO `spacenk_user`(`username`, `reviews`, `location`, `age`, `gender`, `skin_type`, `hair_length`, `hair_color`, `hair_goal`, `skin_tone`, `hair_type`, `skincare_concern`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (username, reviews, location, age, gender, skin_type, hair_length, hair_color, hair_goal, skin_tone, hair_type, skincare_concern)
            #         try:
            #             # Execute the SQL command
            #             cursor.execute(userinfo_insert_sql)
            #             # Commit your changes in the database
            #             db.commit()
            #         except:
            #             # Rollback in case there is any error
            #             db.rollback()
            # except:
            #     print ("Error: unable to fetch data")
            
            insert_review_sql = "INSERT INTO `spacenk_review`(`review_date`, `product_url`, `brand`, `category`, `product`, `rating`, `bestuse`, `recommend_product`, `review_title`, `review_content`, `input_date`, `username`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" % (review_date, product_url, brand, category, product, review_rating, bestuse, recommend_product, review_title, review_content, currentday, username)
            try:
                # Execute the SQL command
                cursor.execute(insert_review_sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        try:
            nextbutton = driver.find_element_by_class_name('bv-content-btn.bv-content-btn-pages.bv-content-btn-pages-last.bv-focusable.bv-content-btn-pages-active')
            nextbutton.click()
            time.sleep(4)
            get_next_data(driver, brand, product, category, product_url)
        except:
            driver.close()
    except:
        driver.close()
def get_next_data(driver, brand, product, category, product_url):
 
    try:
        soup = BeautifulSoup(driver.page_source,"html.parser")
        data = soup.find('div', attrs={'class':'bv-content-list-container'})
        try:
            rowdata = data.find_all('li', attrs={'class':'bv-content-item bv-content-top-review bv-content-review'})
            for j in range(len(rowdata)):
                # userdata = rowdata.find('div', attrs={'class':'bv-author-profile'})
                try:
                    username = rowdata[j].find('div', attrs={'class':'bv-content-author-name'}).text
                except:
                    username = ''
                try:
                    reviews = rowdata[j].find('span', attrs={'class':'bv-author-userstats-value'}).text
                except:
                    reviews = ''
                try:
                    location = rowdata[j].find('div', attrs={'class':'bv-author-location'}).text
                except:
                    location = ''
                print('username: ' + username)
                print('reviews: ' + reviews)
                print('location: ' + location)
                try:
                    userinfo_data = rowdata[j].find_all('span', attrs={'class':'bv-author-userinfo-data'})
                    userinfo_value = rowdata[j].find_all('span', attrs={'class':'bv-author-userinfo-value'})
                    
                    for i in range(len(userinfo_data)):
                        # print(userinfo_data[i])
                        age = ''
                        gender = ''
                        skin_type = ''
                        hair_length = ''
                        hair_color = ''
                        hair_goal = ''
                        skin_tone = ''
                        hair_type = ''
                        skincare_concern = ''
                        if userinfo_data[i].text == 'Age':
                            age = userinfo_value[i].text
                            print('age: '+age)
                        elif userinfo_data[i].text == 'Gender':
                            gender = userinfo_value[i].text
                            print('gender: '+gender)
                        elif userinfo_data[i].text == 'Skin Type:':
                            skin_type = userinfo_value[i].text
                            print('skin_type: '+skin_type)
                        elif userinfo_data[i].text == 'What is your hair length?':
                            hair_length = userinfo_value[i].text
                            print('hair_length: '+hair_length)
                        elif userinfo_data[i].text == 'What is your hair colour?':
                            hair_color = userinfo_value[i].text
                            print('hair_color: '+hair_color)
                        elif userinfo_data[i].text == 'What is your hair goal?':
                            hair_goal = userinfo_value[i].text
                            print('hair_goal: ' + hair_goal)
                        elif userinfo_data[i].text == 'Skin Tone:':
                            skin_tone =  userinfo_value[i].text
                            print('skin_tone: '+skin_tone)
                        elif userinfo_data[i].text == 'Hair Type:':
                            hair_type = userinfo_value[i].text
                            print('hair_type: ' + hair_type)
                        elif userinfo_data[i].text == 'Skincare Concern:':
                            skincare_concern = userinfo_value[i].text
                            print('skincare_concern: '+skincare_concern)
                except:
                    age = ''
                    gender = ''
                    skin_type = ''
                    hair_length = ''
                    hair_color = ''
                    hair_goal = ''
                    skin_tone = ''
                    hair_type = ''
                    skincare_concern = ''
                try:
                    review_date = rowdata[j].find('span', attrs={'class':'bv-content-datetime-stamp'}).text
                except:
                    review_date = ''
                print('review_date: ' + review_date)
                try:
                    review_rating = rowdata[j].find('span', attrs={'class':'bv-off-screen'}).text
                    review_rating_array = review_rating.split()
                    review_rating = review_rating_array[0]
                except:
                    review_rating = ''
                print('review_rating: '+review_rating)
                try:
                    bestuse_temp = rowdata[j].find_all('li', attrs={'class':'bv-content-data-value'})
                    bestuse = ''
                    for i in range(len(bestuse_temp)):
                        bestuse = bestuse + bestuse_temp[i].text
                except:
                    bestuse = ''
                print('bestuse: ' + bestuse)
                try:
                    recommend_product = rowdata[j].find_all('span', attrs={'class':'bv-content-data-label'})
                    recommend_product = recommend_product[1].text
                except:
                    recommend_product = ''
                print('recommend_product: '+recommend_product)
                try:
                    review_title = rowdata[j].find('h3', attrs={'class':'bv-content-title'}).text
                except:
                    review_title = ''
                print('review_title: ' + review_title)
                try:
                    review_content = rowdata[j].find('div', attrs={'class':'bv-content-summary-body-text'}).text
                except:
                    review_content = ''
                print('review_content: ' + review_content)
                currentday = date.today()
                print("current_day: " + str(currentday))
                currentday = str(currentday)
                username = textskin(username)
                location = textskin(location)
                age = textskin(age)
                gender = textskin(gender)
                skin_type = textskin(skin_type)
                hair_length = textskin(hair_length)
                hair_color = textskin(hair_color)
                hair_goal = textskin(hair_goal)
                skin_tone = textskin(skin_tone)
                hair_type = textskin(hair_type)
                review_date = textskin(review_date)
                bestuse = textskin(bestuse)
                recommend_product = textskin(recommend_product)
                review_title = textskin(review_title)
                review_content = textskin(review_content)
                
                sql = "SELECT * FROM `spacenk_user` WHERE `username`='%s'" % (username)
                try:
                    # Execute the SQL command
                    # cursor.execute(sql)
                
                    
                    cursor.execute(sql)
                    # Fetch all the rows in a list of lists.
                    # rows = cursor.fetchmany(size=1)
                    results = cursor.fetchall()
                    row_counts = len(results)
                    
                    if row_counts > 0:
                        print('user already existed')
                    else:
                        userinfo_insert_sql = "INSERT INTO `spacenk_user`(`username`, `reviews`, `location`, `age`, `gender`, `skin_type`, `hair_length`, `hair_color`, `hair_goal`, `skin_tone`, `hair_type`, `skincare_concern`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (username, reviews, location, age, gender, skin_type, hair_length, hair_color, hair_goal, skin_tone, hair_type, skincare_concern)
                        try:
                            # Execute the SQL command
                            cursor.execute(userinfo_insert_sql)
                            # Commit your changes in the database
                            db.commit()
                        except:
                            # Rollback in case there is any error
                            db.rollback()
                except:
                    print ("Error: unable to fetch data")
                
                insert_review_sql = "INSERT INTO `spacenk_review`(`review_date`, `product_url`, `brand`, `category`, `product`, `rating`, `bestuse`, `recommend_product`, `review_title`, `review_content`, `input_date`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (review_date, product_url, brand, category, product, review_rating, bestuse, recommend_product, review_title, review_content, currentday)
                try:
                    # Execute the SQL command
                    cursor.execute(insert_review_sql)
                    # Commit your changes in the database
                    db.commit()
                except:
                    # Rollback in case there is any error
                    db.rollback()
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            match=False
            while(match==False):
                lastCount = lenOfPage
                time.sleep(1)
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True
            try:
                nextbutton = driver.find_element_by_class_name('bv-content-btn.bv-content-btn-pages.bv-content-btn-pages-last.bv-focusable.bv-content-btn-pages-active')
                nextbutton.click()
                time.sleep(4)
                get_next_data(driver, brand, product, category, product_url)
            except:
                driver.close()
        except:
            driver.close()
    except:
        driver.close()
def product_info(url):
    driver = webdriver.Chrome(executable_path='E:/scrapping_jack/Mirabeauty/chromedriver')
    driver.get(url)
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source,"html.parser")
    brand = soup.find('span', attrs={'class':'product-brand'}).text.strip()
    print('brand: ' + brand)
    product = soup.find('h1', attrs={'class':'product-name'}).text.strip().split(' by')[0]
    print('product: ' + product)
    try:
        category_temp = soup.find('ul', attrs={'class':'breadcrumb'}).find_all('a')
        category = ''
        for i in range(3):
            if i > 0:
                category = category + ' > ' + category_temp[i].text.strip()
            else:
                category = category_temp[i].text.strip()
    except:
        category = ''
    print('category: ' + category)
    # get_data(soup, driver, brand, product, category, url)
    try:
        
        data = soup.find('div', attrs={'class':'bv-content-list-container'})
        rowdata = data.find_all('li', attrs={'class':'bv-content-item bv-content-top-review bv-content-review'})
        for j in range(len(rowdata)):
            # userdata = rowdata.find('div', attrs={'class':'bv-author-profile'})
            try:
                username = rowdata[j].find('div', attrs={'class':'bv-content-author-name'}).text
            except:
                username = ''
            try:
                reviews = rowdata[j].find('span', attrs={'class':'bv-author-userstats-value'}).text
            except:
                reviews = ''
            try:
                location = rowdata[j].find('div', attrs={'class':'bv-author-location'}).text
            except:
                location = ''
            print('username: ' + username)
            print('reviews: ' + reviews)
            print('location: ' + location)
            try:
                userinfo_data = rowdata[j].find_all('span', attrs={'class':'bv-author-userinfo-data'})
                userinfo_value = rowdata[j].find_all('span', attrs={'class':'bv-author-userinfo-value'})
                
                for i in range(len(userinfo_data)):
                    # print(userinfo_data[i])
                    age = ''
                    gender = ''
                    skin_type = ''
                    hair_length = ''
                    hair_color = ''
                    hair_goal = ''
                    skin_tone = ''
                    hair_type = ''
                    skincare_concern = ''
                    if userinfo_data[i].text == 'Age':
                        age = userinfo_value[i].text
                        print('age: '+age)
                    elif userinfo_data[i].text == 'Gender':
                        gender = userinfo_value[i].text
                        print('gender: '+gender)
                    elif userinfo_data[i].text == 'Skin Type:':
                        skin_type = userinfo_value[i].text
                        print('skin_type: '+skin_type)
                    elif userinfo_data[i].text == 'What is your hair length?':
                        hair_length = userinfo_value[i].text
                        print('hair_length: '+hair_length)
                    elif userinfo_data[i].text == 'What is your hair colour?':
                        hair_color = userinfo_value[i].text
                        print('hair_color: '+hair_color)
                    elif userinfo_data[i].text == 'What is your hair goal?':
                        hair_goal = userinfo_value[i].text
                        print('hair_goal: ' + hair_goal)
                    elif userinfo_data[i].text == 'Skin Tone:':
                        skin_tone =  userinfo_value[i].text
                        print('skin_tone: '+skin_tone)
                    elif userinfo_data[i].text == 'Hair Type:':
                        hair_type = userinfo_value[i].text
                        print('hair_type: ' + hair_type)
                    elif userinfo_data[i].text == 'Skincare Concern:':
                        skincare_concern = userinfo_value[i].text
                        print('skincare_concern: '+skincare_concern)
            except:
                age = ''
                gender = ''
                skin_type = ''
                hair_length = ''
                hair_color = ''
                hair_goal = ''
                skin_tone = ''
                hair_type = ''
                skincare_concern = ''
            try:
                review_date = rowdata[j].find('span', attrs={'class':'bv-content-datetime-stamp'}).text
            except:
                review_date = ''
            print('review_date: ' + review_date)
            try:
                review_rating = rowdata[j].find('span', attrs={'class':'bv-off-screen'}).text
                review_rating_array = review_rating.split()
                review_rating = review_rating_array[0]
            except:
                review_rating = ''
            print('review_rating: '+review_rating)
            try:
                bestuse_temp = rowdata[j].find_all('li', attrs={'class':'bv-content-data-value'})
                bestuse = ''
                for i in range(len(bestuse_temp)):
                    bestuse = bestuse + bestuse_temp[i].text
            except:
                bestuse = ''
            print('bestuse: ' + bestuse)
            try:
                recommend_product = rowdata[j].find_all('span', attrs={'class':'bv-content-data-label'})
                recommend_product = recommend_product[1].text
            except:
                recommend_product = ''
            print('recommend_product: '+recommend_product)
            try:
                review_title = rowdata[j].find('h3', attrs={'class':'bv-content-title'}).text
            except:
                review_title = ''
            print('review_title: ' + review_title)
            try:
                review_content = rowdata[j].find('div', attrs={'class':'bv-content-summary-body-text'}).text
            except:
                review_content = ''
            print('review_content: ' + review_content)
            currentday = date.today()
            print("current_day: " + str(currentday))
            currentday = str(currentday)
            username = textskin(username)
            location = textskin(location)
            age = textskin(age)
            gender = textskin(gender)
            skin_type = textskin(skin_type)
            hair_length = textskin(hair_length)
            hair_color = textskin(hair_color)
            hair_goal = textskin(hair_goal)
            skin_tone = textskin(skin_tone)
            hair_type = textskin(hair_type)
            review_date = textskin(review_date)
            bestuse = textskin(bestuse)
            recommend_product = textskin(recommend_product)
            review_title = textskin(review_title)
            review_content = textskin(review_content)

            sql = "SELECT * FROM `spacenk_user` WHERE `username`='%s'" % (username)
            try:
                # Execute the SQL command
                # cursor.execute(sql)
            
                
                cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                # rows = cursor.fetchmany(size=1)
                results = cursor.fetchall()
                row_counts = len(results)
                
                if row_counts > 0:
                    print('user already existed')
                else:
                    userinfo_insert_sql = "INSERT INTO `spacenk_user`(`username`, `reviews`, `location`, `age`, `gender`, `skin_type`, `hair_length`, `hair_color`, `hair_goal`, `skin_tone`, `hair_type`, `skincare_concern`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (username, reviews, location, age, gender, skin_type, hair_length, hair_color, hair_goal, skin_tone, hair_type, skincare_concern)
                    try:
                        # Execute the SQL command
                        cursor.execute(userinfo_insert_sql)
                        # Commit your changes in the database
                        db.commit()
                    except:
                        # Rollback in case there is any error
                        db.rollback()
            except:
                print ("Error: unable to fetch data")
            
            insert_review_sql = "INSERT INTO `spacenk_review`(`review_date`, `product_url`, `brand`, `category`, `product`, `rating`, `bestuse`, `recommend_product`, `review_title`, `review_content`, `input_date`, `username`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" % (review_date, url, brand, category, product, review_rating, bestuse, recommend_product, review_title, review_content, currentday, username)
            try:
                # Execute the SQL command
                cursor.execute(insert_review_sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        try:
            nextbutton = driver.find_element_by_class_name('bv-content-btn.bv-content-btn-pages.bv-content-btn-pages-last.bv-focusable.bv-content-btn-pages-active')
            nextbutton.click()
            time.sleep(4)
            get_next_data(driver, brand, product, category, url)
        except:
            driver.close()
    except:
        driver.close()

# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
# product_info('https://www.spacenk.com/eu/skincare/toner/toners/ready-steady-glow-daily-aha-tonic-MUK300051309.html')

def extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    data = soup.find('ul',attrs={'class':'search-result-items tiles-container clearfix hide-compare js-initial-load-result'})
    product_data = data.find_all('a', attrs={'class':'product-tile_link--image thumb-link js-set-scroll-value js-thumb-link'})
    for i in range(len(product_data)):
        product_url = product_data[i].get('href')
        print(product_url)
        product_info(product_url)
        



brand_url = 'https://www.spacenk.com/eu/brands'
brand_page = requests.get(brand_url)
brand_soup = BeautifulSoup(brand_page.content,"html.parser")
brand_soup_content = brand_soup.find('ul',attrs={'class':'blp-list js-brands-list'})
brand_a_contents = brand_soup_content.find_all('a', attrs={'class':'blp-link'})
for i in range(len(brand_a_contents)):
    brand_a_href = brand_a_contents[i].get('href')
    print(brand_a_href)
    brand_a_content = brand_a_contents[i].text
    print(brand_a_content)
    extract(brand_a_href)
    

db.close()