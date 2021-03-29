# python-package

            ______________
            ___________(_)__  /
            ___  /____  /__  / 
            __  /____  / _  /  
            _____/__  /  /_/   
               /___/  2021 day day up
     
    python常用的一些类包汇总说明，目的构建清晰知识体系，基于python3一些简单的demo

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

- 文本处理

    - string -- 字符串常量和模板
    - textwrap -- 文本段落格式化 
    - re -- 正则表达式
    - difflib -- 字符比较
    
- 数据结构

    - enum -- 枚举类型
    - collections --- 数据类型容器
    - array --- 序列化的固定类型结构
    - heapq -- 堆排序算法
    - bisect --- 维护有序列表 r
    - queue --- 线程安全的 FIFO 队列
    - struct --- 二进制数据结构
    - weakref --- 实现对象的弱引用
    - copy --- 对象复制
    - pprint --- 格式化输出数据结构
    
- 算法

    - functools --- 函数操作工具箱
    - itertools --- 迭代器函数
    - operator --- 内置操作符接口
    - contextlib --- 上下文管理器工具

- 日期和时间
    
    - time --- 时间模块
    - datetime --- 日期和时间处理
    - calendar --- 日期操作
    
- 数学模块
    
    - decimal --- 高精度计算模块
    - fractions --- 分数运算
    - random --- 伪随机数生成器
    - math --- 数学函数
    - statistics --- 统计学计算
 
- 文件系统操作
    
    - os.path --- 跨平台的文件名操作
    - pathlib --- 文件路径对象
    - glob --- 文件名规则匹配
    - fnmatch --- Unix 风格的 Glob 规则匹配
    - linecache --- 高效率文件读取
    - tempfile --- 临时文件对象
    - shutil --- 高阶文件操作
    - filecmp --- 文件对比
    - mmap --- 内存映射模块
    - codecs --- 字符编码和解码
    - io --- 文本、二进制和原生流的 I/O 工具

- 数据持久化和数据交换

    - pickle — 对象序列华
    - shelve — 实例对象的持久化
    - dbm — Unix 键值数据库
    - sqlite3 — 嵌入式关系型数据库
    - xml.etree.ElementTree — XML 操作接口
    - csv — 「逗号分隔值」文件
 
- 数据压缩和归档   

    - zlib — GNU zlib 压缩
    - gzip — 读写 GNU zip 文件
    - bz2 — bzip2 压缩格式
    - tarfile — 访问 Tar 格式的文件
    - zipfile — 访问 Zip 格式的文件

- 加密服务
    
    - hashlib — 加密哈希算法
    - hmac — 加密消息签名和验证
       
- **并行运算**

    - subprocess --- 创建新进程
    - signal --- 异步系统事件
    - threading --- 多线程并发处理,进程内并发操作的管理
    - multiprocessing --- 多进程并发处理，类似多线程
    - asyncio --- 协程并发处理,异步 I/O，事件循环以及并发工具
    - concurrent.futures --- 并发任务管理池

- 网络模块

    - ipaddress — 互联网地址
    - socket — 互联网通讯
    - selectors — I/O 多路复用抽象层
    - select — 高效地等待 I/O
    - socketserver — 创建网络服务器

- 互联网数据处理
   
    - urllib.parse --- 将 URLs 拆分为各个组成部...
    - urllib.request --- 访问网络资源
    - urllib.robotparser --- 网络爬虫访问控制
    - base64 --- 用 ASCII 编码二进制数据
    - http.server --- 实现网络服务器的基本工具类
    - http.cookies --- HTTP Cookies
    - webbrowser --- 渲染展示网页
    - uuid --- 通用唯一标识符
    - json --- JavaScript Object Notation
    - xmlrpc.client — XML-RPC 客户端类库
    - xmlrpc.server --- 一个 XML-RPC 服务器

- 邮件模块

    - smtplib --- SMTP 协议客户端
    - smtpd --- SMTP 服务器
    - mailbox --- 管理 Email 规定文件
    - imaplib --- IMAP4 客户端类库

- 应用程序组成元素

    - argparse --- 命令行选项和参数解析
    - getopt --- 命令行选项解析
    - readline --- GNU readline 库
    - getpass --- 安全密码提示
    - cmd --- 面向行的命令处理器
    - shlex --- 解析 Shell 样式的语法
    - configparser --- 使用配置文件
    - logging --- 报告状态、错误和信息性消息
        - [example](./example/logging/)
        > 日志文件生成管理函数库。级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
                                                                            
        > [logbook](https://github.com/getlogbook/logbook) logging的替换品,有兴趣的可以自己看看
    - fileinput --- 命令行过滤器框架
    - atexit --- 程序关闭回调
    - sched --- 定时事件调度程序

- 国际化和本地化

    - locale — 本地人文接口
    - gettext — 翻译消息
 
- 开发者工具

   - pydoc --- 模块的线上帮助文档
   - doctest --- 通过文档来测试的模块
   - unittest --- 自动化测试框架
   - trace --- 追踪程序流
   - traceback --- 异常和栈追踪
   - cgitb --- 详细的追踪报告
   - pdb --- 交互式调试器
   - profile and pstats --- 性能分析器
   - timeit --- 小块代码的时间测试
   - tabnanny --- 缩进终结者
   - compileall --- 原文件字节编译器
   - pyclbr --- 类浏览器
   - venv --- 虚拟环境
   - ensurepip --- 安装 Python 包安装器

- 运行时服务

    - site — 整站范围内的配置信息
    - sys — 系统范围内的配置信息
    - os — 便捷地访问操作系统专属功能 
    - platform — 系统版本信息
    - resource — 系统资源管理
    - gc — 垃圾收集器
    - sysconfig — 命令解释器编译时配置

- 语言工具

    - warnings --- 非致命警报
    - abc --- 抽象基类
    - dis --- Python 字节码反编译程序
    - inspect --- 审查活动元素

- 模块和扩展包

    - importlib — Python 的模块载入机制
    - pkgutil — 扩展包工具
    - zipimport — 从 Zip 文件中加载 Python 代码

- Unix 专属的服务
 
    - pwd --- Unix 密码数据库
    - grp --- Unix 用户组数据库

## 算法
- pybloom_live 布隆过滤器
    
    - [example](./example/pybloom_live/)

    > pybloom_live下面有俩个方法，BloomFilter（定容）和ScalableBloomFilter（可伸缩的）。
     
    > 是一种以bitmap集合为基础的投影去重算法，其应用场景如Url的排重，垃圾邮箱地址的过滤等邻域

    > 布隆算法的核心思想就是对url进行多次不同算法的hash，得到不同的hashcode，最后再将这些hashcode比较后映射到同一个bitmap上

## 数据

- NumPy

    > NumPy是使用Python进行科学计算的基础软件包。除其他外，它包括：
        功能强大的N维数组对象。
        精密广播功能函数。
        集成 C/C+和Fortran 代码的工具。
        强大的线性代数、傅立叶变换和随机数功能。
          
- pandas
    > pandas是基于NumPy数组构建的，使数据预处理、清洗、分析工作变得更快更简单。pandas是专门为处理表格和混杂数据设计的，而NumPy更适合处理统一的数值数组数据。

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
      填充持久性以进行压力测试还是匿名化从生产服务中获取的数据，Faker都是您的理想

- [Supervisor](https://github.com/Supervisor/supervisor)

    > 一套通用的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启。
    通过fork/exec的方式把这些被管理的进程当作supervisor的子进程来启动，这样只要在supervisor的配置文件中，
    把要管理的进程的可执行文件的路径写进去即可。也实现当子进程挂掉的时候，父进程可以准确获取子进程挂掉的信息的，
    可以选择是否自己启动和报警。supervisor还提供了一个功能，可以为supervisord或者每个子进程，
    设置一个非root的user，这个user就可以管理它对应的进程。

## 知识点

- 序列(Sequence)

    > 一种数据结构，这种数据结构根据索引来获取序列中的对象。
    Python3中含有三种内建序列类型：list, tuple, string, range。
    其中range比较特殊，它是一个生成器，其他几个类型具有的一些序列特性对它并不适合，不做详述。

    - 序列切片
         
        > 切片操作就是对序列按照给定的索引和步长，截取序列中由连续对象组成的片段。
        对于序列结构来说，索引和步长都有正负值，分别表示左右两个方向
                                                               
            - 索引的正方向从左往右取值，起始位置为0，有效范围为 [0, 序列长度-1]
            - 索引的负方向从右往左取值，起始位置为-1，有效范围为 [-序列长度, -1] 
            
        > 因此任意一个序列结构数据的索引范围为-序列长度到序列长度-1范围内的连续整数。
        
    - Sequence [start_index: end_index: step] 切片操作语法
        - start：表示是第一个元素对象，正索引位置默认为0；负索引位置默认为 -序列长度
        - end：表示是最后一个元素对象，正索引位置默认为 序列长度－1；负索引位置默认为 -1
        - step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值，默认为1，步长值不能为0
    - example  字符串和list效果类似
        ```
        x = '1234'
        print(x[:-5:-1]) #输出4321
        print(x[::-1]) #输出4321
        print(str[:0:-1]) #输出432
        print(str[:0:-2]) #输出42
        print(str[0::1]) #输出1234
        print(str[0::2]) #输出13
        ```
                                              