# -*-encoding:utf-8-*-
'''
1. 安装pytesseract
　　pip3 insatll pytesseract -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
2. 安装pillow
　　pip3 install pillow -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
3. 安装Tesseract-OCR(https://github.com/tesseract-ocr/tesseract)
4. 安装完后将Tesseract-OCR的安装路径添加到环境变量中PATH和Path中都要添加
'''
import pytesseract
import os
from PIL import Image


def main():
    # print os.getcwd() #获取当前工作目录路径
    # print os.path.abspath('.') #获取当前工作目录路径
    #使用当前文件的相对路径，使用工作路径找不到文件 bug 20200127
    relative_path = os.path.dirname(os.path.abspath(__file__))
    image = Image.open('{}/demo.png'.format(relative_path))
    #image.show() #打开图片 demo.png
    text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
    print(text) #识别出来的文字

if __name__ == '__main__':
    main()

'''
print 内容如下
python常用的一些类包站
明都是基于python3写的或者直引用的一些官方demo,pip3安装我用的是淘宝的源,争取每日更新一个吧^ ^
'''