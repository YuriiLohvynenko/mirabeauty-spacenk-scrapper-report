import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT `id`, `category` FROM `spacenk_listing` ORDER BY id ASC"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        category_id = row[0] 
        category = row[1]
        try:
            category_temp = category.split(' > ')
            real_category = category_temp[1]
        except: 
            real_category = ''
        update_sql = "UPDATE `spacenk_listing` SET `real_category`='%s' WHERE `id`='%d'" % (real_category, category_id)
        try:
            # Execute the SQL command
            cursor.execute(update_sql)
            print("done: " + str(category_id))
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()