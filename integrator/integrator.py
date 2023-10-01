import redis
import time

time.sleep(30)

pool = redis.ConnectionPool(host='db-redis', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)


redis.set('mykey', 'Hello from Python!')
value = redis.get('mykey')
print(value)

redis.zadd('vehicles', {'car' : 0})
redis.zadd('vehicles', {'bike' : 0})
vehicles = redis.zrange('vehicles', 0, -1)
print(vehicles)