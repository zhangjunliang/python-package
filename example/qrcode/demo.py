# -*-encoding:utf-8-*-
'''
安装 pip3 insatll qrcode -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
'''

#生产矢量图二维码
import os
import qrcode.image.svg

img_file = '{}/demo.svg'.format(os.path.dirname(os.path.abspath(__file__)))

img = qrcode.make('https://github.com/zhangjunliang/python-package',image_factory=qrcode.image.svg.SvgImage)

img.save(img_file)