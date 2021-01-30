# -*-encoding:utf-8-*-
"""
1. 安装
　　pip3 paramiko pillow -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
"""
import paramiko
import os
import logging
import platform
from stat import S_ISDIR


# 简单实现sftp上传

class sftp(object):
    sftp_host = '192.168.75.177'
    sftp_port = '22'
    sftp_username = 'test'
    sftp_password = '123456'

    def __init__(self):
        # 设置paramiko log 日志级别
        #paramiko_log = paramiko.util.get_logger('paramiko')
        #paramiko_log.setLevel(logging.DEBUG)

        manager = paramiko.Transport(sock=(self.sftp_host, int(self.sftp_port)))
        manager.connect(username=self.sftp_username, password=self.sftp_password)
        self.client = paramiko.SFTPClient.from_transport(manager)

    def __del__(self):

        self.client.close()

    # sftp 根据上传文件路径创建多级目录 最多支持四级
    def mkdir(self, remote_file):
        upload_path = os.path.dirname(remote_file)
        try:
            self.client.chdir(upload_path + '/')
        except IOError as e:
            print(e)

    # 上传单个文件到指定目录下
    def put(self, local_file, remote_file):
        return self.client.put(local_file, remote_file)

    # 判断是否是dir
    def isdir(self, path):
        try:
            return S_ISDIR(self.client.stat(path).st_mode)
        except IOError:
            return False

    # 删除
    def rm(self, path):
        files = self.client.listdir(path=path)
        for f in files:
            filepath = os.path.join(path, f)
            if platform.system() == "Windows":
                filepath = filepath.replace('\\', '/')

            if self.isdir(filepath):
                self.rm(filepath)
            else:
                self.client.remove(filepath)

        self.client.rmdir(path)

if __name__ == '__main__':
    sftp = sftp()

    local_file = 'c:\\test.png'

    #注意：远程地址可能和sftp配置有关系有的是从根目录开始，有的是从sftp配置的根目录开始

    remote_file = '/upload/demo.png'

    result = sftp.put(local_file,remote_file)

    print(result)
    '''
    C:\work_py\python-package>python example\paramiko\sftp.py
    -rw-r--r--   1 1001     1002        19675 30 Jan 11:17 ?
    '''