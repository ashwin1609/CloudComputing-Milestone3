import redis        # pip install redis
ip=""
r = redis.Redis(host=ip, port=6379, db=1,password='SOFE4630U')
v=r.get('key1');
print(v);
r.set('key1','30'.encode('utf-8'));
