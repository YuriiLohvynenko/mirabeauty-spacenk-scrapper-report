import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","mirabeauty_scraper" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT `id`, `price` FROM `listing` WHERE `price`<>''"
try:
    # Execute the SQL command
    # cursor.execute(sql)
   
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    for row in results:
        field_id = row[0]
        price = row[1]
        real_price = price.replace("$", "")
        update_sql = "UPDATE `listing` SET `real_price`='%s' WHERE `id`='%d'" % (real_price, field_id)
        try:
            # Execute the SQL command
            cursor.execute(update_sql)
            print("done")
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

except:
    print ("Error: unable to fetch data")


# disconnect from server
db.close()