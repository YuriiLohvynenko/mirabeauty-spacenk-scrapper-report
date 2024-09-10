import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT `id`, trim(`username`), `category` FROM `spacenk_review` ORDER BY id ASC"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        review_id = row[0] 
        username = row[1]
        category = row[2]
        try:
            category_temp = category.split(' > ')
            real_category = category_temp[1]
        except: 
            real_category = ''
        location_get_sql = "SELECT `location` FROM `spacenk_user` WHERE trim(`username`)='%s'" % (username)
        try:
            cursor.execute(location_get_sql)
            location_results = cursor.fetchall()
            for location_row in location_results:
                location = location_row[0]

                update_sql = "UPDATE `spacenk_review` SET `location`='%s', `real_category`='%s' WHERE `id`='%d'" % (location, real_category, review_id)
                try:
                    # Execute the SQL command
                    cursor.execute(update_sql)
                    print("done: " + str(review_id))
                    # Commit your changes in the database
                    db.commit()
                except:
                    # Rollback in case there is any error
                    db.rollback()
        except:
            print("error")

        
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()