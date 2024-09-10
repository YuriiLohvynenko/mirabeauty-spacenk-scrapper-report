import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT `id`, `username` FROM `category_combination` WHERE `id`>16949 ORDER BY id ASC"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        category_id = row[0] 
        username = row[1]
        category_get_sql = "SELECT `real_category`, COUNT(`id`) FROM `spacenk_review` WHERE `real_category`<>'' AND trim(`username`)='%s' GROUP BY `real_category`" % (username)
        try:
            cursor.execute(category_get_sql)
            category_results = cursor.fetchall()
            for category_row in category_results:
                category = category_row[0]
                total_count = category_row[1]
                print(category)
                update_sql = "UPDATE `category_combination` SET "+ category +"='%s' WHERE `id`='%d'" % (total_count, category_id)
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
            print("error")

        
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()