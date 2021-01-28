# -*-encoding:utf-8-*-
'''
1. 安装Pillow
　　pip3 insatll pillow -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
'''


from PIL import ImageGrab
import os
#截取当前屏幕
img = ImageGrab.grab()
#保存图片
img_file = '{}/demo.png'.format(os.path.dirname(os.path.abspath(__file__)))
img.save(img_file)
#展示截取内容
img.show()