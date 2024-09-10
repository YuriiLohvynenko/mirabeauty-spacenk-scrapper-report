import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT DISTINCT trim(`username`) AS user_name FROM `spacenk_review` WHERE `real_category`<>'' ORDER BY `username` ASC"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    cols = 0
    for row in results:
        cols = cols + 1 
        username = row[0]
        insert_sql = "INSERT INTO `category_combination`(`username`) VALUES ('%s')" % (username)
        try:
            # Execute the SQL command
            cursor.execute(insert_sql)
            print("done" + str(cols))
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()