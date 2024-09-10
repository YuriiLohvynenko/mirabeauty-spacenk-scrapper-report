import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM `listing1` ORDER BY id ASC"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      brand = row[1]
      category = row[2]
      product = row[3]
      price = row[4]
      rating = row[5]
      review = row[6]
      viewon_first = row[7]
      viewon_link = row[8]
      checkout = row[9]
      fullfilledby = row[10]
      alternative_retailers_first = row[11]
      alternative_retailers_link = row[12]
      review_websites = row[13]
      button_statue = row[14]
      product_url = row[15]

      condition_sql = "SELECT `product_url` FROM `listing` WHERE `product_url`='%s'" % (product_url)
      try:
         # Execute the SQL command
         # cursor.execute(sql)
   
         
         cursor.execute(condition_sql)
         # Fetch all the rows in a list of lists.
         # rows = cursor.fetchmany(size=1)
         condition_results = cursor.fetchall()
         row_counts = len(condition_results)
         
         if row_counts > 0:
            print('existing')
         else:
            insert_sql = ''
            # insert_sql = "INSERT INTO `listing`(`brand`, `category`, `product`, `price`, `rating`, `review`, `viewon_first`, `viewon_link`, `checkout`, `fullfilledby`, `alternative_retailers_first`, `alternative_retailers_link`, `review_websites`, `button_statue`, `product_url`) VALUES ('%s','%s','%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (brand, category, product, price, rating, review, viewon_first, viewon_link, checkout, fullfilledby, alternative_retailers_first, alternative_retailers_link, review_websites, button_statue, product_url)
            try:
                  # Execute the SQL command
                  cursor.execute(insert_sql)
                  print('success')
                  # Commit your changes in the database
                  db.commit()
            except:
                  # Rollback in case there is any error
                  db.rollback()
      except:
            print ("Error: unable to fetch data")
        
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()