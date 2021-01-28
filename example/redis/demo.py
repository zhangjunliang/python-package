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

client = redis.Redis(host=host, password=password, port=int(port), db=db, encoding=encoding, decode_responses= decode_responses)

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