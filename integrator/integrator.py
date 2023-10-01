import redis
import time
import psycopg2
from datetime import datetime, timedelta

time.sleep(30)

conn = psycopg2.connect(
    host="db-postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)
cursor = conn.cursor()


# connection to Redis database
redis_conn = redis.StrictRedis(host="db-redis", port=6379, db=0)

# Function to retrieve data from PostgreSQL
def fetch_data():
    select_query = '''
    SELECT user_id, course_id, generated_at FROM dane;
    '''
    cursor.execute(select_query)
    return cursor.fetchall()

# Function to add data to Redis (avoiding duplicates)
def add_to_redis(user_id, course_id, generated_at):
    key = f"{user_id}_{course_id}"
    if not redis_conn.exists(key):
        redis_conn.set(key, str(generated_at))
        print(f"Added to Redis: user_id={user_id}, course_id={course_id}, generated_at={generated_at}")
    else:
        print(f"Skipped (already exists): user_id={user_id}, course_id={course_id}, generated_at={generated_at}")

# Downloading data every 15 seconds and adding it to Redis
try:
    while True:
        data = fetch_data()
        for row in data:
            user_id, course_id, generated_at = row
            generated_at = datetime.strftime(generated_at, "%Y-%m-%d %H:%M:%S")
            add_to_redis(user_id, course_id, generated_at)
        time.sleep(15)
except KeyboardInterrupt:
    print("The program was interrupted.")
finally:
    # Closing cursor and connection to PostgreSQL database
    cursor.close()
    conn.close()

#######################################################################


# pool = redis.ConnectionPool(host='db-redis', port=6379, db=0)
# redis = redis.Redis(connection_pool=pool)


# redis.set('mykey', 'Hello from Python!')
# value = redis.get('mykey')
# print(value)

# redis.zadd('vehicles', {'car' : 0})
# redis.zadd('vehicles', {'bike' : 0})
# vehicles = redis.zrange('vehicles', 0, -1)
# print(vehicles)