# python-package
            ______________
            ___________(_)__  /
            ___  /____  /__  / 
            __  /____  / _  /  
            _____/__  /  /_/   
               /___/  2021.01.27
     
    python常用的一些类包汇总说明,基于python3一些简单的demo,争取每日更新一个吧^_^

## virtualenv 虚拟环境

1. virtualenv 
    
    > 为了解决各个项目的共同依赖同一个环境，造成版本冲突等，virtualenv创建一个干净的环境，在这个环境下，进行Python项目的开发等，
      就成为一个个独立的项目，从而避免一系列麻烦，提升开发效率。
    
    > virtualenv 的一个最大的缺点就是：
      每次开启虚拟环境之前要去虚拟环境所在目录下的 bin 目录下 source 一下 activate，这就需要我们记住每个虚拟环境所在的目录。

2. [virtualenvwrapper](./example/virtualenv/README.md)

    > virtualenvwrapper管理你的虚拟环境（virtualenv），其实他就是统一管理虚拟环境的目录，并且省去了source的步骤。
    
3. 建议直接使用 virtualenvwrapper，具体virtualenv的操作就不详细写了

## 标准库

1. logging
    
    - [example](./example/logging/)

    > Python标准库，日志文件生成管理函数库。[logbook](https://github.com/getlogbook/logbook) logging的替换品,
    有兴趣的可以自己看看。级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

## 算法
1. pybloom_live 布隆过滤器
    
    - [example](./example/pybloom_live/)

    > pybloom_live下面有俩个方法，BloomFilter（定容）和ScalableBloomFilter（可伸缩的）。
     
    > 是一种以bitmap集合为基础的投影去重算法，其应用场景如Url的排重，垃圾邮箱地址的过滤等邻域

    > 布隆算法的核心思想就是对url进行多次不同算法的hash，得到不同的hashcode，最后再将这些hashcode比较后映射到同一个bitmap上

## 数据

1. [pymysql](https://github.com/PyMySQL/PyMySQL)
    
    - [example](./example/pymysql/)

    > pymysql是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

2. [redis](https://github.com/WoLpH/redis-py)
    
    - [example](./example/redis/)

    > redis-py 操作redis的库,The Python interface to the Redis key-value store. 

## web框架

1. Django

    > 流行的Python-Web框架，鼓励快速开发,并遵循MVC设计，开发周期短

2. Flask

    > 轻量级web框架

## 爬虫

1. [lxml](https://github.com/lxml/lxml)

    - [example](./example/lxml/)

    > lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式，而且解析效率非常高
    
    - 问题1：Scrapy使用tbody解析不到内容？
        > 原因：html = etree.parse('test.html', parser=parser)
            html = etree.HTML(resposne.text) 二者格式化代码规则可能不同
        
        >建议：如果解析在线网页，不要添加tbody标签，
            反则解析本地(离线)网页，添加tbody标签
    
2. Scrapy

    > 快速屏幕截取和网页抓取的框架,实话实说用了这个可能你就不想用别的了

## 图像处理

1. [Pillow](https://github.com/python-pillow/Pillow)

    - [example](./example/pillow/)

    > PIL：Python Imaging Library，图像处理标准库,功能非常强大，API非常简单易用。由于PIL仅支持到Python 2.7，
    加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多
    新特性，建议直接安装使用Pillow。

2. [Tesseract OCR光学字符识别](https://github.com/madmaze/pytesseract)

    - [example](./example/tesseract/)

    > python的光学字符识别（OCR）工具，识别并“读取”图像中嵌入的文本，是Google Tesseract-OCR Engine的包装。
    可以用作tesseract的独立调用脚本，可以读取Pillow和Leptonica图像库支持的所有图像类型，包括jpeg，png，
    gif，bmp，tiff等。此外，打印和识别的文本，而不是将其写入文件。                                                                                                        >

3. qrcode 二维码生成

    - [python-qrcode](https://github.com/lincolnloop/python-qrcode)
    - [example](./example/qrcode/)
    > 二维码（QR码）生成器,支持矢量图生成

    - [myqr 二维码](https://github.com/sylnsfar/qrcode)
    - demo可以自己去搜索
    > 可生成普通二维码、带图片的艺术二维码（黑白与彩色）、动态二维码（黑白与彩色）
                                                                                                

## 机器学习

1. TensorFlow

    > 谷歌基于DistBelief进行研发的第二代人工智能学习系统。

## 其他

1. Paramiko 

    [example](./example/paramiko/)

    > ssh是一个协议，OpenSSH是其中一个开源实现，paramiko是Python的一个库，实现了SSHv2协议(底层使用cryptography)。
    
    > 有了Paramiko以后，我们就可以在Python代码中直接使用SSH协议对远程服务器执行操作，而不是通过ssh命令对远程服务器进行操作。
    
2. Cryptography
    
    > Cryptography的目标是建立一个标准Python加密库，支持 Python 2.6-2.7, Python 3.3+, and PyPy 2.6+。
  
3. [Faker](https://github.com/joke2k/faker)
    
    > Faker是一个Python软件包，可为您生成伪造数据。无论您是需要引导数据库，创建美观的XML文档，
      填充持久性以进行压力测试还是匿名化从生产服务中获取的数据，Faker都是您的理想之选。                                                                                                   