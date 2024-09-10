import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql

def textskin(text):
    return text.replace("'","@@@").replace('"','###')

def product_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    brand = soup.find('span', attrs={'class':'product-brand'}).text.strip()
    print('brand: ' + brand)
    product = soup.find('h1', attrs={'class':'product-name'}).text.strip().split(' by')[0]
    print('product: ' + product)
    try:
        product_number_data = soup.find('div', attrs={'class':'product-number'})
        size = product_number_data.text.split(' |')[0].strip()
        if 'SKU#' in size:
            size = ''
        sku = product_number_data.find('span').text.strip().replace('M','')
    except:
        size = ''
        sku = ''
    print('size: ' + size)
    print('SKU: ' + sku)
    try:
        price = soup.find('div', attrs={'class':'product-price'}).text.strip().split(' - ')[1].replace('.','')
    except:
        price = '0'
    if price == '0':
        try:
            price = soup.find('span', attrs={'class':'price-sales'}).text.strip().replace('.','')
        except:
            price = '0'
    if price == 'N/A':
        price = '0'
    price = price.replace('€ ','').replace(',','.')
    print('price: ' + price)
    try:
        rating = soup.find('span', attrs={'class':'bvseo-ratingValue'}).text.strip()
    except:
        rating = '0'
    print('rating: ' + rating)
    try:
        review = soup.find('span', attrs={'class':'bvseo-reviewCount'}).text.strip()
    except:
        review = '0'
    print('review: ' + review)
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
    try:
        product_option_number_temp = soup.find('fieldset', attrs={'class':'swatches size'})
        
        product_option_number = str(len(product_option_number_temp.find_all('div')))
    except:
        product_option_number = ''
    
    print('product_option_number: ' + product_option_number)
    brand = textskin(brand)
    category = textskin(category)
    product = textskin(product)
    size = textskin(size)
    price = float(price)
    rating = float(rating)
    reviews = float(review)
    product_url = textskin(url)

    sql = "INSERT INTO `spacenk_listing`(`brand`, `category`, `product`, `size`, `price`, `product_option_number`, `sku`, `rating`, `reviews`, `product_url`) VALUES ('%s','%s','%s','%s','%f','%s','%s','%f','%f','%s')" % (brand, category, product, size, price, product_option_number, sku, rating, reviews, product_url)
    
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
# product_info('https://www.spacenk.com/eu/haircare/hair-treatment/hair-treatment/no.-3-hair-perfector-MUK300053878.html?dwvar_MUK300053878_size=UK300053878')
def extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    data = soup.find('ul',attrs={'class':'search-result-items tiles-container clearfix hide-compare js-initial-load-result'})
    product_data = data.find_all('a', attrs={'class':'product-tile_link--image thumb-link js-set-scroll-value js-thumb-link'})
    for i in range(len(product_data)):
        product_url = product_data[i].get('href')
        print(product_url)
        sql = "SELECT `product_url` FROM `spacenk_listing` WHERE `product_url`='%s'" % (product_url)
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
        


# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

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