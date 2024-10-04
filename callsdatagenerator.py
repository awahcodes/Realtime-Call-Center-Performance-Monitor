import datetime
import time
import random
import mysql.connector
from mysql.connector import Error

# Database configuration
config = {
    'user': 'root',
    'password': 'Onajourney123#',
    'host': '127.0.0.1',  # MySQL server IP 
    'database': 'Call_Center',  # database name
    'raise_on_warnings': True
}

connection = None  # Initialize the connection variable

# Connect to the database
try:
    connection = mysql.connector.connect(**config)
    print("Connection to MySQL DB successful!")

    # Create a cursor object
    cursor = connection.cursor()

    # Run a loop which will never end to generate random calls
    while True:
        date = datetime.datetime.now()

        # Generate random values
        location = random.randint(111, 201)
        company = random.randint(11, 30)
        issue = random.randint(111, 130)
        csr = random.randint(111, 210)
        rtime = random.randint(1, 300)
        ctime = random.randint(1, 600)
        status = random.randint(1, 4)

        #we want to have our status  being mostly resolved issues. Thus, over 7% of the random generated will be resolved since it's equal 1
        # if status < 75:
        #   status = 1
        # elif status < 85:
        #   status = 2
        # elif status < 90:
        #   status = 3
        # else:
        #   status = 4

        # Depending on the status value, a random rating is generated
        if status == 1:
            rating = random.randint(5, 10)
        elif status == 2:
            rating = random.randint(3, 10)
        elif status == 3:
            rating = random.randint(1, 3)
        elif status == 4:
            rating = random.randint(1, 5)

        # Inserting the generated values into the database
        insert_query = """
        INSERT INTO calls (date, location_id, company_id, issue_id, csr_id, response_time, call_time, status, rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (date, location, company, issue, csr, rtime, ctime, status, rating))

        # Commiting the transaction
        connection.commit()

        # Print the generated values
        print(date, location, company, issue, csr, rtime, ctime, status, rating)

        # Delay loop by 1 second by every iteration
        time.sleep(1)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        print("MySQL connection is closed.")
