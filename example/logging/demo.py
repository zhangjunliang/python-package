# -*- coding: UTF-8 -*-

"""
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上
info : 打印info,warning,error,critical级别的日志,确认一切按预期运行
warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作
error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
"""

import logging
import os
import sys


class DemoLog(object):

    result = {'code': 100, 'message': None, 'data': None}

    def __init__(self, log_filename, level=logging.DEBUG):
        # 创建logger，如果参数为空则返回root logger
        logger = logging.getLogger('demo')
        # 设置logger日志等级
        logger.setLevel(level)
        # 创建handler 设置编码 保证中文不乱码
        fh = logging.FileHandler(log_filename, encoding='utf-8', mode='a') #文件
        ch = logging.StreamHandler() #不设置不会打印输出
        # 设置输出日志格式
        log_formatter = logging.Formatter(
            fmt='%(asctime)s %(name)s %(process)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        # 为handler指定输出格式，注意大小写
        fh.setFormatter(log_formatter)
        ch.setFormatter(log_formatter)
        # 为logger添加的日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logging = logger


    def log(self, level, code=9999, message=None, data=None):
        self.result['code'] = code
        self.result['message'] = message
        self.result['data'] = data

        self.logging.log(level, self.result)


if __name__ == '__main__':
    log_file = '{}/demo.log'.format(os.path.dirname(os.path.abspath(__file__)))

    demo = DemoLog(log_file)

    demo.log(logging.DEBUG, 0, '打印全部的日志, 详细的信息, 通常只出现在诊断问题上', {'debug': '调式信息'})
    demo.log(logging.INFO, 1, '打印info, warning, error, critical级别的日志, 确认一切按预期运行', {'data': '数据'})
    demo.log(logging.WARNING, 2,
             '打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作',
             {'warning': '警告'})
    demo.log(logging.ERROR, 3, '打印error, critical级别的日志, 更严重的问题, 软件没能执行一些功能', {'Exception': 'Error Exception'})
    demo.log(logging.CRITICAL, 4, '打印critical级别, 一个严重的错误, 这表明程序本身可能无法继续运行', {'Exception': 'Error Exception'})
