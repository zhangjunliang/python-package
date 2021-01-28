# -*-encoding:utf-8-*-
"""
1. 安装lxml
　　pip3 lxml pillow -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com

获取demo html中所有的图片地址
"""
from lxml import etree
import os

demo_file = '{}/demo.html'.format(os.path.dirname(os.path.abspath(__file__)))

img = []
with open(demo_file, 'r', encoding='utf-8') as f:
    content = f.read()
    html = etree.HTML(content)
    img_list = html.xpath('//img')
    for i in range(0, len(img_list)):
        tmp_src = img_list[i].xpath('./@src')
        if len(tmp_src) >0:
            img.append(tmp_src[0])

print(img)
'''
['https://pic.qiushibaike.com/system/avtnew/1299/12992639/thumb/20201115205001.jpg?imageView2/1/w/90/h/90', 'https://static.qiushibaike.com/images/newarticle/like@
1.5.png?v=b7f830b3bb97b559891af61444d3b4ad', 'https://pic.qiushibaike.com/system/avtnew/3603/36030904/thumb/20201215154650.jpg?imageView2/1/w/90/h/90', 'https://st
atic.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad', 'https://pic.qiushibaike.com/system/avtnew/4048/40484754/thumb/20201016103
900.jpg?imageView2/1/w/90/h/90', 'https://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad', 'https://pic.qiushibaike.com/s
ystem/avtnew/3239/32395436/thumb/20171013142058.JPEG?imageView2/1/w/90/h/90', 'https://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891a
f61444d3b4ad', 'https://pic.qiushibaike.com/system/avtnew/3857/38575320/thumb/20190810202656.jpg?imageView2/1/w/90/h/90', 'https://static.qiushibaike.com/images/ne
warticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad', 'https://pic.qiushibaike.com/system/avtnew/1187/11878716/thumb/20190520091055.jpg?imageView2/1/w/90/h/90
', 'https://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad', 'https://pic.qiushibaike.com/system/avtnew/3435/34350130/thu
mb/20200908075439.jpg?imageView2/1/w/90/h/90', 'https://static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad']
'''