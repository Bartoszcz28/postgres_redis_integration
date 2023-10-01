import psycopg2
from datetime import datetime, timedelta
import time
import random

time.sleep(30)
conn = psycopg2.connect(
    host="db-postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)


cursor = conn.cursor()


create_table_query = '''
CREATE TABLE IF NOT EXISTS dane (
    id SERIAL PRIMARY KEY,
    user_id INT,
    course_id INT,
    generated_at TIMESTAMP
);
'''
cursor.execute(create_table_query)
conn.commit()


def generate_data():
    user_id = random.randint(1, 100)
    course_id = random.randint(1, 4)
    generated_at = datetime.now()
    return user_id, course_id, generated_at

def insert_data(user_id, course_id, generated_at):
    insert_query = '''
    INSERT INTO dane (user_id, course_id, generated_at)
    VALUES (%s, %s, %s);
    '''
    cursor.execute(insert_query, (user_id, course_id, generated_at))
    conn.commit()

try:
    while True:
        user_id, course_id, generated_at = generate_data()
        insert_data(user_id, course_id, generated_at)
        print(f"Generated record: user_id={user_id}, course_id={course_id}, generated_at={generated_at}")
        time.sleep(15)
except KeyboardInterrupt:
    print("Program został przerwany.")
finally:
    cursor.close()
    conn.close()
