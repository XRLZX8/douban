#-*- coding = utf-8 -*-
"""
@author: XRL
@software: PyCharm
@file: testSqlite.py
@time: 2020/6/28 17:31
"""
import sqlite3

# conn = sqlite3.connect("test.db")   #打开或创建数据库文件
#
# print('成功打开数据库')
# c = conn.cursor()   #获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
#
# c.execute(sql)  #执行sql
# conn.commit()#提交数据库操作
# conn.close()#关闭数据库连接
# print('成功建表')


#3.插入数据
# conn = sqlite3.connect("test.db")
# c = conn.cursor()   #获取游标
#
# sql1 = '''
#     insert into company(id, name, age, address, salary)
#     values (1,'xxx',22,'awddasdawdasda',10000)
#     ;
# '''
#
# sql2 = '''
#     insert into company(id, name, age, address, salary)
#     values (2,'ccc',22,'awdasdawdghhj',12000)
#     ;
# '''
#
# c.execute(sql1)
# c.execute(sql2)#执行sql
# conn.commit()#提交数据库操作
# conn.close()#关闭数据库连接
# print('数据插入成功')

#4.查询数据
conn = sqlite3.connect("test.db")
c = conn.cursor()   #获取游标

sql1 = '''
    select id, name, age, address, salary from company 
    ;
'''
cursor = c.execute(sql1)

for row in cursor:
    print('id=',row[0])
    print('name=', row[1])
    print('age=', row[2])
    print('adderss=', row[3],'\n')