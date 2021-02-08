# python-package
            ______________
            ___________(_)__  /
            ___  /____  /__  / 
            __  /____  / _  /  
            _____/__  /  /_/   
               /___/  2021.01.27
     
    python常用的一些类包汇总说明,基于python3一些简单的demo,争取每日更新一个吧^_^

## [Python库打包分发](./example/setuptools/README.md)
    
- [setuptools](https://github.com/pypa/setuptools)
    
    - [example](./example/setuptools/)
    
    - setuptools 是 python 的基础包工具，可以帮助我们轻松的下载，构建，安装，升级，卸载 python的软件包。
    
    - Python库打包的格式包括Wheel和Egg。Egg格式是由setuptools在2004年引入，而Wheel格式是由PEP427在2012年定义。
    使用Wheel和Egg安装都不需要重新构建和编译，其在发布之前就应该完成测试和构建。
    
    - Egg和Wheel本质上都是一个zip格式包，Egg文件使用.egg扩展名，Wheel使用.whl扩展名。
    Wheel的出现是为了替代Egg，其现在被认为是Python的二进制包的标准格式。
    
- pip vs easy_install

   - easy_install是setuptool包提供的第三方包安装工具，而pip是easy_install的改进版。老版本的python中只有easy_install，没有pip。

   - pip相对于easy_install进行了以下几个方面的改进:
    
        - 所有的包是在安装之前就下载了，所以不可能出现只安装了一部分的情况
        - 在终端上的输出更加友好
        - 对于动作的原因进行持续的跟踪。例如，如果一个包正在安装，那么pip就会跟踪为什么这个包会被安装
        - 错误信息会非常有用
        - 代码简洁精悍可以很好的编程
        - 不必作为egg存档，能扁平化安装(仍然保存egg元数据)
        - 原生的支持其他版本控制系统(Git,MercurialandBazaar)
        - 加入卸载包功能
        - 可以简单的定义修改一系列的安装依赖，还可以可靠的赋值一系列依赖包

## virtualenv 虚拟环境

- virtualenv 
    
    > 为了解决各个项目的共同依赖同一个环境，造成版本冲突等，virtualenv创建一个干净的环境，在这个环境下，进行Python项目的开发等，
      就成为一个个独立的项目，从而避免一系列麻烦，提升开发效率。
    
    > virtualenv 的一个最大的缺点就是：
      每次开启虚拟环境之前要去虚拟环境所在目录下的 bin 目录下 source 一下 activate，这就需要我们记住每个虚拟环境所在的目录。

- [virtualenvwrapper](./example/virtualenv/README.md)

    > virtualenvwrapper管理你的虚拟环境（virtualenv），其实他就是统一管理虚拟环境的目录，并且省去了source的步骤。
    
- 建议直接使用 virtualenvwrapper，具体virtualenv的操作就不详细写了

## 标准库/内置模块
  
- multiprocessing
    
    多进程并发处理
     
- threading

    多线程并发处理
    
- asyncio模块

    协程并发处理
            
- logging
    
    - [example](./example/logging/)

    > Python标准库，日志文件生成管理函数库。[logbook](https://github.com/getlogbook/logbook) logging的替换品,
    有兴趣的可以自己看看。级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

## 算法
- pybloom_live 布隆过滤器
    
    - [example](./example/pybloom_live/)

    > pybloom_live下面有俩个方法，BloomFilter（定容）和ScalableBloomFilter（可伸缩的）。
     
    > 是一种以bitmap集合为基础的投影去重算法，其应用场景如Url的排重，垃圾邮箱地址的过滤等邻域

    > 布隆算法的核心思想就是对url进行多次不同算法的hash，得到不同的hashcode，最后再将这些hashcode比较后映射到同一个bitmap上

## 数据

- [pymysql](https://github.com/PyMySQL/PyMySQL)
    
    - [example](./example/pymysql/)

    > pymysql是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

- [redis](https://github.com/WoLpH/redis-py)
    
    - [example](./example/redis/)

    > redis-py 操作redis的库,The Python interface to the Redis key-value store. 

## web框架

- Django

    > 流行的Python-Web框架，鼓励快速开发,并遵循MVC设计，开发周期短

- Flask

    > 轻量级web框架

## 爬虫

- [lxml](https://github.com/lxml/lxml)

    - [example](./example/lxml/)

    > lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式，而且解析效率非常高
    
    - 问题1：Scrapy使用tbody解析不到内容？
        > 原因：html = etree.parse('test.html', parser=parser)
            html = etree.HTML(resposne.text) 二者格式化代码规则可能不同
        
        >建议：如果解析在线网页，不要添加tbody标签，
            反则解析本地(离线)网页，添加tbody标签
    
- Scrapy

    > 快速屏幕截取和网页抓取的框架,实话实说用了这个可能你就不想用别的了

- Selenium 
    
    > Selenium是一系列基于Web的自动化工具，提供一套测试函数，用于支持Web自动化测试。函数非常灵活，
    能够完成界面元素定位、窗口跳转、结果比较。支持多款主流浏览器，提供了功能丰富的API接口，经常被我们用作爬虫工具来使用。
    
    > selenium的缺点也很明显，比如速度太慢、对版本配置要求严苛，最麻烦是经常要更新对应的驱动。
    还有些网页是可以检测到是否是使用了selenium。并且selenium所谓的保护机制不允许跨域cookies
    保存以及登录的时候必须先打开网页然后后加载cookies再刷新的方式很不友好。

- Pyppeteer [_2018年9月份之后几乎没更新过,导致很多bug根本没人修复_]
    
    - 另一款web自动化测试工具，支持的浏览器比较单一，但在安装配置的便利性和运行效率方面都要远胜selenium。
    
    - Puppeteer是Google基于Node.js开发的一个工具，主要是用来操纵Chrome浏览器的API，
      通过Javascript代码来操纵Chrome浏览器的一些操作，用作网络爬虫完成数据爬取、Web程序自动测试等任务。其API极其完善，功能非常强大。
    
    - 而Pyppeteer实际上是Puppeteer的Python版本的实现，但他不是Google开发的，
      是一位来自于日本的工程师依据Puppeteer的一些功能开发出来的非官方版本。

- PyExecJS、PyV8、Js2Py

    - PyExecJS
    
        > 主要是将JS代码运行在本地的JS环境中，优点是我们有多种JS环境的选择，官方推荐了PyV8、Node.js、PhantomJS、Nashorn四种，
        当然缺点是必须安装一种环境导致不是很轻量，而且调用时有一个启动环境过程，还是有明显缓慢的
    
    - PyV8
        
        > Google官方将ChromeV8引擎用Python封装的库，和`PyExecJS`相比，
        这个库很轻量，不需要额外装JS环境，因为V8本身就是环境，同时也因为不需要启动外部环境，执行速度很快。
        
    - Js2Py
    
        > 将 JS 代码直接转译成 Python 代码，这种方式可以摆脱调用 JS 环境的瓶颈，
        但遗憾的是如果用于很长的混淆 JS 代码，转译过来的大概率会报错… 
    

## 图像处理

- [Pillow](https://github.com/python-pillow/Pillow)

    - [example](./example/pillow/)

    > PIL：Python Imaging Library，图像处理标准库,功能非常强大，API非常简单易用。由于PIL仅支持到Python 2.7，
    加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多
    新特性，建议直接安装使用Pillow。

- [Tesseract OCR光学字符识别](https://github.com/madmaze/pytesseract)

    - [example](./example/tesseract/)

    > python的光学字符识别（OCR）工具，识别并“读取”图像中嵌入的文本，是Google Tesseract-OCR Engine的包装。
    可以用作tesseract的独立调用脚本，可以读取Pillow和Leptonica图像库支持的所有图像类型，包括jpeg，png，
    gif，bmp，tiff等。此外，打印和识别的文本，而不是将其写入文件。                                                                                                        >

- Qrcode 二维码生成

    - [python-qrcode](https://github.com/lincolnloop/python-qrcode)
    - [example](./example/qrcode/)
    > 二维码（QR码）生成器,支持矢量图生成

    - [myqr 二维码](https://github.com/sylnsfar/qrcode)
    - demo可以自己去搜索
    > 可生成普通二维码、带图片的艺术二维码（黑白与彩色）、动态二维码（黑白与彩色）
                                                                                                

## 机器学习

- TensorFlow

    > 谷歌基于DistBelief进行研发的第二代人工智能学习系统。

## 其他

- Paramiko 

    [example](./example/paramiko/)

    > ssh是一个协议，OpenSSH是其中一个开源实现，paramiko是Python的一个库，实现了SSHv2协议(底层使用cryptography)。
    
    > 有了Paramiko以后，我们就可以在Python代码中直接使用SSH协议对远程服务器执行操作，而不是通过ssh命令对远程服务器进行操作。
    
- Cryptography
    
    > Cryptography的目标是建立一个标准Python加密库，支持 Python 2.6-2.7, Python 3.3+, and PyPy 2.6+。
  
- [Faker](https://github.com/joke2k/faker)
    
    > Faker是一个Python软件包，可为您生成伪造数据。无论您是需要引导数据库，创建美观的XML文档，
      填充持久性以进行压力测试还是匿名化从生产服务中获取的数据，Faker都是您的理想之选。                                                                                                   