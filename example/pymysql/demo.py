# -*-encoding:utf-8-*-
'''
1. 安装pymysql
　　pip3 insatll pymysql -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
'''
import pymysql

class DemoDb(object):

    host = '127.0.0.1'
    port = '3306'
    user = 'root'
    password = '123456'
    database = 'python_package'
    charset = 'utf8'
    timeout = '30'

    def __init__(self):
        self.conn = pymysql.connect(host= self.host, port=int(self.port), user=self.user, password=self.password, database=self.database, charset=self.charset, connect_timeout=int(self.timeout))

    def __del__(self):
        self.conn.close()
        pass

    # 获取一条
    def get_one(self, sql, *args):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql,args)
        return cursor.fetchone()

    # 获取列表
    def get_all(self, sql, *args):
        #返回字段名称
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql,args)
        return list(cursor.fetchall())

    # 更新数据
    def update_one(self, sql, *args):
        cursor = self.conn.cursor()
        status = cursor.execute(sql, args)
        self.conn.commit()
        return status

    # 插入更新多条
    def update_more(self, sql, items):
        cursor = self.conn.cursor()
        cursor.executemany(sql, items)
        self.conn.commit()
        return

    # 创建查询更新事务
    def select_and_update(self, s_sql, u_sql):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.conn.begin()
        cursor.execute(s_sql)
        a = list(cursor.fetchall())
        b = tuple([i['id'] for i in a])
        if len(b) == 1:
            b = str(b).replace(',', '')
        elif len(b) > 1:
            b = str(b)
        else:
            return []
        cursor.execute(u_sql + b)
        self.conn.commit()
        return a

if __name__ == '__main__':
    DemoDb = DemoDb()
    #获取一条数据
    sql_one = 'select * from users where id =%s limit 1'
    one_result = DemoDb.get_one(sql_one,1)
    print(one_result)
    '''
    {'id': 1, 'name': '张三', 'age': 10, 'status': 0}
    '''
    #更新一条数据
    sql_one = 'update users set name=%s where id =%s limit 1'
    update_result = DemoDb.update_one(sql_one, '小四' ,1)
    print(update_result)
    '''
    1
    '''
    # 获取所有数据
    sql_all = 'select * from users'
    all_result = DemoDb.get_all(sql_all)
    print(all_result)
    '''
    [{'id': 1, 'name': '小四', 'age': 5, 'status': 0}, {'id': 2, 'name': '哈哈', 'age': 5, 'status': 0}]
    '''
    # 创建查询更新事务
    select_sql = "select * from users where status = 0 for update"
    update_sql = "update users set status = '2' where id in "
    result = DemoDb.select_and_update(select_sql,update_sql)
    print(result)
    '''
    [{'id': 1, 'name': '小四', 'age': 5, 'status': 0}, {'id': 2, 'name': '哈哈', 'age': 5, 'status': 0}]
    '''