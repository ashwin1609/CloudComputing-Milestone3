import redis        # pip install redis
ip='172.31.71.218';
r = redis.Redis(host=ip, port=6379, db=1,password='SOFE4630U')
v=r.get('OntarioTech');
with open("./recieved.jpg", "wb") as f:
    f.write(v);
