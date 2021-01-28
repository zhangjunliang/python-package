# -*- coding: UTF-8 -*-

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

'''
通常情况下, 当我们需要做redis操作时, 会创建一个连接, 并基于这个连接进行redis操作, 操作完成后, 释放连接,
一般情况下, 这是没问题的, 但当并发量比较高的时候, 频繁的连接创建和释放对性能会有较高的影响
于是, 连接池就发挥作用了
连接池的原理是, 通过预先创建多个连接, 当进行redis操作时, 直接获取已经创建的连接进行操作, 而且操作完成后, 不会释放, 用于后续的其他redis操作
这样就达到了避免频繁的redis连接创建和释放的目的, 从而提高性能了
'''
# client = redis.Redis(host=host, password=password, port=int(port), db=db, encoding=encoding, decode_responses= decode_responses)
# 使用连接池连接redis
pool = redis.ConnectionPool(host=host, password=password, port=int(port), db=db, encoding=encoding, decode_responses= decode_responses)
client = redis.Redis(connection_pool=pool)

status = client.set('demo', 'demo')
print(status)
'''
True
'''
data = client.get('demo')
print(data)
'''
demo
'''
