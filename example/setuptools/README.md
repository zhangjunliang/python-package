# Python库打包分发
    
    Python有非常丰富的第三方库可以使用很多开发者会向pypi上提交自己的Python包。
    要想向pypi包仓库提交自己开发的包，首先要将自己的代码打包，才能上传分发。

## 打包

1. distutils 简介

    - distutils是标准库中负责建 Python 第三方库的安装器，使用它能够进行Python模块的安装和发布。
    - distutils对于简单的分发很有用，但功能缺少。大部分Python用户会使用更先进的setuptools模块。

2. setuptools 简介

    - setuptools是distutils增强版，不包括在标准库中。其扩展了很多功能，能够帮助开发者更好的创建和分发Python包。
    大部分Python用户都会使用更先进的setuptools 模块。

    - distribute【setuptools的fork分支】它们共享相同的命名空间，因此如果安装了distribute，
    import setuptools时实际上将导入使用distribute创建的包。Distribute已经合并回setuptools。

    - distutils2大包分发工具【不及预期，已废弃】，其试图尝试充分利用distutils，detuptools和distribute并成为Python标准库中的标准工具。

    因此，setuptools 是一个优秀的，可靠的 Pthon 包安装与分发工具。以下设计到包的安装与分发均针对setuptools，并不保证distutils可用。   

## 包格式
1.
    > Python库打包的格式包括Wheel和Egg。Egg格式是由setuptools在2004年引入，而Wheel格式是由PEP427在2012年定义。
    使用Wheel和Egg安装都不需要重新构建和编译，其在发布之前就应该完成测试和构建。
    
    > Egg和Wheel本质上都是一个zip格式包，Egg文件使用.egg扩展名，Wheel使用.whl扩展名。
    Wheel的出现是为了替代Egg，其现在被认为是Python的二进制包的标准格式

    - 以下是 Wheel 和 Egg 的主要区别：
    
        - Wheel 有一个官方的 PEP427 来定义，而 Egg 没有 PEP 定义
        - Wheel 是一种分发格式，即打包格式。而 Egg 既是一种分发格式，也是一种运行时安装的格式，并且是可以被直接 import
        - Wheel 文件不会包含 .pyc 文件
        - Wheel 使用和 PEP376 兼容的 .dist-info 目录，而 Egg 使用 .egg-info 目录
        - Wheel 有着更丰富的命名规则。
        - Wheel 是有版本的。每个 Wheel 文件都包含 wheel 规范的版本和打包的实现
        - Wheel 在内部被 sysconfig path type 管理，因此转向其他格式也更容易
    详细描述可见：[Wheel vs Egg](https://packaging.python.org/discussions/wheel-vs-egg/)
    
## setup.py文件
    
1. Python库打包分发的关键在于编写setup.py文件。setup.py文件编写的规则是从setuptools导入setup函数，并传入各类参数进行调用。  
   
    ``` 
    # -*- coding: utf-8 -*-
    from setuptools import setup
    # or
    # from distutils.core import setup  
    setup(
            name='demo',     # 包名字
            version='v1.0',   # 包版本
            description='This is a test of the setup',   # 简单描述
            author='zjl',  # 作者
            author_email='779581051@qq.com',  # 作者邮箱
            url='https:https://github.com/zhangjunliang/python-package',      # 包的主页
            packages=['demo'],                 # 包
    )
    ```
   
2. setup.py函数常用参数说明：

    参数|说明
    ----|----
    name|包名称
    version|包版本
    author|程序的作者
    author_email|程序的作者的邮箱地址
    maintainer|维护者
    maintainer_email|维护者的邮箱地址
    url|程序的官网地址
    license|程序的授权信息
    description|程序的简单描述
    long_description|程序的详细描述
    platforms|程序适用的软件平台列表
    classifiers|程序的所属分类列表
    keywords|程序的关键字列表
    packages|需要处理的包目录(通常为包含 init.py 的文件夹)
    py_modules|需要打包的 Python 单文件列表
    download_url|程序的下载地址
    cmdclass|添加自定义命令
    package_data|指定包内需要包含的数据文件
    include_package_data|自动包含包内所有受版本控制(cvs/svn/git)的数据文件
    exclude_package_data|当 include_package_data 为 True 时该选项用于排除部分文件
    data_files|打包时需要打包的数据文件，如图片，配置文件等
    ext_modules|指定扩展模块
    scripts|指定可执行脚本,安装时脚本会被安装到系统 PATH 路径下
    package_dir|指定哪些目录下的文件被映射到哪个源码包
    requires|指定依赖的其他包
    provides|指定可以为哪些模块提供依赖
    install_requires|安装时需要安装的依赖包
    entry_points|动态发现服务和插件，下面详细讲
    setup_requires|指定运行 setup.py 文件本身所依赖的包
    dependency_links|指定依赖包的下载地址
    extras_require|当前包的高级/额外特性需要依赖的分发包
    zip_safe|不压缩包，而是以目录的形式安装
    
    更多参数可见：https://setuptools.readthedocs.io/en/latest/setuptools.html

3. find_packages 函数
    
    > 对于简单工程来说，手动增加 packages 参数是容易。而对于复杂的工程来说，可能添加很多的包，这是手动添加就变得麻烦。
      Setuptools 模块提供了一个 find_packages 函数,它默认在与 setup.py 文件同一目录下搜索各个含有 init.py 的目录做为要添加的包。

    > find_packages(where='.', exclude=(), include=('*',))

    > find_packages 函数的第一个参数用于指定在哪个目录下搜索包，参数 exclude 用于指定排除哪些包，参数 include 指出要包含的包。

    > 默认情况下 setup.py 文件只在其所在的目录下搜索包。如果不用 find_packages，想要找到其他目录下的包，
      也可以设置 package_dir 参数，其指定哪些目录下的文件被映射到哪个源码包，
      如: package_dir={'': 'src'} 表示 “root package” 中的模块都在 src 目录中。

4. 包含数据文件
    
    > package_data：该参数是一个从包名称到 glob 模式列表的字典。如果数据文件包含在包的子目录中，则 glob 可以包括子目录名称。其格式一般为 {'package_name': ['files']}，比如：package_data={'mypkg': ['data/*.dat'],}。
    
    > include_package_data：该参数被设置为 True 时自动添加包中受版本控制的数据文件，可替代 package_data，同时，exclude_package_data 可以排除某些文件。注意当需要加入没有被版本控制的文件时，还是仍然需要使用 package_data 参数才行。
    
    > data_files：该参数通常用于包含不在包内的数据文件，即包的外部文件，如：配置文件，消息目录，数据文件。其指定了一系列二元组，即(目的安装目录，源文件) ，表示哪些文件被安装到哪些目录中。如果目录名是相对路径，则相对于安装前缀进行解释。
    
    > manifest template：manifest template 即编写 MANIFEST.in 文件，文件内容就是需要包含在分发包中的文件。一个 MANIFEST.in 文件如下：
    
        include *.txt
        recursive-include examples *.txt *.py
        prune examples/sample?/build
        MANIFEST.in 文件的编写规则可参考：https://docs.python.org/3.6/distutils/sourcedist.html

