# -*-encoding:utf-8-*-
'''
安装 pip3 insatll pybloom_live -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
'''

from pybloom_live import BloomFilter,ScalableBloomFilter
import bisect

def str_filesize(size):
    d = [(1024-1,'K'), (1024**2-1,'M'), (1024**3-1,'G'), (1024**4-1,'T')]
    s = [x[0] for x in d]
    index = bisect.bisect_left(s, size) - 1
    if index == -1:
        return str(size)
    else:
        b, u = d[index]
    return str(size / (b+1)) + u

#定长
bf = BloomFilter(capacity=10000)
print(bf.count)

for i in range(0,12):
    try:
        bf.add("zjl-{}".format(i))
    except Exception as e:

        print(i,e)
a,b,c,d,e = bf.bitarray.buffer_info()
print(a,b,c,d,str_filesize(b))

import redis
#地址
host = '127.0.0.1'
#密码
password = '123456'
#端口
port = 6379
#第几个库
db = 0
#编码
encoding = 'utf-8'
#Python3下Redis默认返回bytes类型数据，而Python3下bytes类型和str类型不能直接互用，容易出错，解决方法是在建立Redis连接的时候将decode_responses设置为True，表示将返回的bytes数据解码为str数据
decode_responses = True

# client = redis.Redis(host=host, password=password, port=int(port), db=db, encoding=encoding, decode_responses= decode_responses)
# 使用连接池连接redis
pool = redis.ConnectionPool(host=host, password=password, port=int(port), db=db, encoding=encoding, decode_responses= decode_responses)
client = redis.Redis(connection_pool=pool)

for hash in list(bf.make_hashes('http://www.voidcn.com/article/p-qbftgdpd-bqc.html'.encode("utf-8"))):
    client.setbit('ant_US_www_disa_mil_zhangwuji_3', hash ,1)


print("zjl-1" in bf)   # True
print("zjl-15" in bf)  # False



#扩容的方式 SMALL_SET_GROWTH 小量 LARGE_SET_GROWTH 大量
sbf = ScalableBloomFilter(initial_capacity=10, error_rate=0.001, mode=ScalableBloomFilter.LARGE_SET_GROWTH)

url = "皮卡丘1"
url2 = "皮卡丘2"

sbf.add(url)

print(url in sbf)   # True
print(url2 in sbf)  # False