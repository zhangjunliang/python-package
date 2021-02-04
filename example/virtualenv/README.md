# virtualenv 虚拟环境

### 针对virtualenvwrapper的命令，virtualenv自己百度就能看到

    --python是指定python的版本

1. 安装
    
    - 虚拟环境
    > pip3 install virtualenv 
    
    - virtualenvwrapper管理你的虚拟环境（virtualenv）
    > pip3 install virtualenvwrapper
    - windows 需要安装  
    > pip3 install virtualenvwrapper-win 
    
    - 设置环境变量
    > WORKON_HOME 虚拟环境工作根目录
    
2. 创建虚拟环境

    - mkvirtualenv gerapy
    - 如果需要指定版本 mkvirtualenv --python3[win下是python.ext的路径] gerapy 
    
    - 针对环境安装依赖
    > pip3 install c:\Twisted-20.3.0-cp38-cp38-win_amd64.whl
    
    > pip3 install gerapy -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
    
    - 启动gerapy
    > gerapy runserver
    
3. 进入虚拟环境
    - workon gerapy 
    
4. - 停止虚拟环境
    - deactivate
    
5. 删除虚拟环境
   -  rmvirtualenv gerapy
    
6. 其他
   - 列举所有的环境
   > lsvirtualenv
   - 导航到当前激活的虚拟环境的目录中，比如说这样您就能够浏览它的 site-packages
   > cdvirtualenv
   - 和上面的类似，但是是直接进入到 site-packages 目录中。
   > cdsitepackages
   - 显示 site-packages 目录中的内容
   > lssitepackages

                                                                                                                                                                                                 
    