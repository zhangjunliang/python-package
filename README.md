# python-package
            ______________
            ___________(_)__  /
            ___  /____  /__  / 
            __  /____  / _  /  
            _____/__  /  /_/   
               /___/  2021.01.27
     
    python常用的一些类包汇总说明,基于python3一些简单的demo,争取每日更新一个吧^_^

## 标准库

### logging
[example](./example/logging/)

Python标准库，日志文件生成管理函数库。[logbook](https://github.com/getlogbook/logbook) logging的替换品,有兴趣的可以自己看看。
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

## 数据

### [pymysql](https://github.com/PyMySQL/PyMySQL)
[example](./example/pymysql/)

pymysql是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。


### [redis](https://github.com/WoLpH/redis-py)
[example](./example/redis/)

redis-py 操作redis的库,The Python interface to the Redis key-value store. 

## web框架

### Django

流行的Python-Web框架，鼓励快速开发,并遵循MVC设计，开发周期短

### Flask

轻量级web框架

## 爬虫

### Scrapy

快速屏幕截取和网页抓取的框架

## 图像处理


### Pillow

PIL：Python Imaging Library，图像处理标准库,功能非常强大，API非常简单易用。由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，建议直接安装使用Pillow。
### [Tesseract OCR光学字符识别](https://github.com/madmaze/pytesseract)
[example](./example/tesseract/)

python的光学字符识别（OCR）工具，识别并“读取”图像中嵌入的文本，是Google Tesseract-OCR Engine的包装。可以用作tesseract的独立调用脚本，可以读取Pillow和Leptonica图像库支持的所有图像类型，包括jpeg，png，gif，bmp，tiff等。此外，打印和识别的文本，而不是将其写入文件。

## 机器学习

### TensorFlow

谷歌基于DistBelief进行研发的第二代人工智能学习系统。