
# logger
import logging

# Step 1: Create a custom logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)  # Set the lowest level you want to capture

# Step 2: Create handlers
file_handler = logging.FileHandler("app.log", mode='w')  # 'w' to overwrite each run
console_handler = logging.StreamHandler()

file_handler.setLevel(logging.DEBUG)     # Log everything to file
console_handler.setLevel(logging.CRITICAL)   # Only show INFO+ in console

# Step 3: Create formatter and add it to handlers
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Step 4: Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Step 5: Use the logger
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning!")
# logger.error("Error occurred!")
# logger.critical("Critical failure!")

logger.info("========== System up")

import sqlite3
import os

# check if file exists
try:
    if os.path.exists('db1.db'):
        os.remove('db1.db')  # delete file
        logger.info('db file removed')
    else:
        logger.debug('db file was not found')
except Exception as e:
    logger.error(f"failed to delete file, {e}")

conn = sqlite3.connect('db1.db')
conn.row_factory = sqlite3.Row  # ...magic ...
cursor = conn.cursor()
logger.info('db ready')

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);
''')

logger.info('table created')

# 3
# safe - multiple query
data = [
    (1, 'Paul', 32, 'California', 20000.00),
    (2, 'Allen', 25, 'Texas', 15000.00),
    (3, 'Teddy', 23, 'Norway', 20000.00),
    (4, 'Mark', 25, 'Rich-Mond ', 65000.00),
    (5, 'David', 27, 'Texas', 85000.00),
    (6, 'Kim', 22, 'South-Hall', 45000.00),
]
cursor.executemany('''
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (?, ?, ?, ?, ?);
''', data)
logger.info("inserted 6 rows")
logger.debug('''
INSERTED:
 (1, 'Paul', 32, 'California', 20000.00),
    (2, 'Allen', 25, 'Texas', 15000.00),
    (3, 'Teddy', 23, 'Norway', 20000.00),
    (4, 'Mark', 25, 'Rich-Mond ', 65000.00),
    (5, 'David', 27, 'Texas', 85000.00),
    (6, 'Kim', 22, 'South-Hall', 45000.00),
''')

# solution:
logger.info("starting to insert data from user")
while True:
    try:
        new_id = int(input('enter id:'))
        new_name = input('enter name:')
        new_age = int(input('enter age:'))
        new_address = input('enter address:')
        new_salary = float(input('enter salary:'))
        logging.debug(f" entered {new_id} {new_name} {new_age} {new_address} {new_salary}")
        cursor.execute('''
        INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
        VALUES (?, ?, ?, ?, ?);
        ''', (new_id, new_name, new_age, new_address, new_salary))
        last_inserted = cursor.lastrowid
        logger.info("inserted completed!")
        break
    except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
        logger.error(f"failed to insert row, {e}")
        print('db error ', e)
    except Exception as e:
        print('=== cannot insert this row. try again ===')
        logger.error(f"failed to insert row, {e}")


conn.commit()  # write changes

conn.close()  # close for safety

logger.info("========== System shut-down")

# try:
#     user_input = input('enter number:')
#     logger.debug(user_input)
#     num = int(user_input)
# except Exception as e:


'''
1. create logger for file + console
2. set console to info, file to debug
3. log.info -> system start
4. input number from user in a loop, until int(input) succeed
   log.debug the user input (before doing int(input))
   for failure log to file the error (try-except)
5. after success log the number   
6. log.info -> system shut-down    
'''