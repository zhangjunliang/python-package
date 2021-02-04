# -*-encoding:utf-8-*-
'''
安装 pip3 insatll pybloom_live -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
'''

from pybloom_live import BloomFilter,ScalableBloomFilter
import bisect
import os

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
bf = BloomFilter(capacity=1000)

#超出报错
for i in range(0,101):
    try:
        bf.add("zjl-{}".format(i))
    except Exception as e:
        print(i,e)

#address, size, endianness, unused, allocated

#布隆过滤器的一些信息
address,size,endianness,unused,allocated = bf.bitarray.buffer_info()

print(address,size,endianness,unused,allocated, str_filesize(size))



print("zjl-1" in bf)   # True
print("zjl-15" in bf)  # False

#字符串的hash值，实际for循环写入bf可以 存redis的时候是一样的
hash_key =list(bf.make_hashes('zjl'.encode(encoding='utf-8')))
# ---
print('hash_key:',hash_key)

#写入某个文件
bf_file = '{}/demo.bytes'.format(os.path.dirname(os.path.abspath(__file__)))
#b 参数可以写入bytes
with open(bf_file,'wb') as f:
    bf.tofile(f)


#扩容的方式 SMALL_SET_GROWTH 小量两倍扩容 LARGE_SET_GROWTH 大量 4倍扩容
sbf = ScalableBloomFilter(initial_capacity=10000, error_rate=0.001, mode=ScalableBloomFilter.SMALL_SET_GROWTH)

#布隆过滤器的一些信息
print(sbf.filters)

# print(sbf_address,sbf_size,sbf_endianness,sbf_unused,sbf_allocated, str_filesize(sbf_size))
#超出自动扩容
for i in range(0,111000):
    try:
        sbf.add("zjl-{}".format(i))
    except Exception as e:
        print(i,e)

for bf in sbf.filters:
    address, size, endianness, unused, allocated = bf.bitarray.buffer_info()
    print(address, size, endianness, unused, allocated, str_filesize(size))


#写入某个文件
sbf_file = '{}/demo_sbf.bytes'.format(os.path.dirname(os.path.abspath(__file__)))

print('zjl-1' in sbf)
#b 参数可以写入bytes
with open(sbf_file,'wb') as f:
    sbf.tofile(f)
