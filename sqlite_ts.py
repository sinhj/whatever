# -*- encoding: utf-8 -*-

import os
import sqlite3
import time



dat_dir = r"."
db_name = "ts"
db_path = os.path.join(dat_dir, db_name) + ".db"

# 判断文件是否存在，如果存在同名目录就删除
if os.path.isfile(db_path):
    print "File \"" + db_path + "\" already exists."
else:
    if os.path.exists(db_path):
        print "Dir \"" + db_path + "\" exists. It will be deleted."
        # try except
        if os.system("rd /Q /S " + db_path) != 0:
            print "A fatal error occurred while deleting."
            exit(-1)
    print "File \"" + db_path + "\" will be created."

# 连接到 SQLite 数据库，如果文件不存在，就会新建
try:
    cnct = sqlite3.connect(db_path)
except sqlite3.OperationalError, err:
    print err
    if str(err).find("unable to open") != -1:
        if not os.path.isfile(db_path):
            print "You don't have permission to access the dir."
        else:
            print "You don't have permission to read this file."
    exit(-1)

# 创建一个 Cursor, 游标是一个数据缓冲区，存放 SQL 语句的执行结果
curd = cnct.cursor()

try:
# 执行一条 SQL 语句，创建 user 表
    curd.execute("create table user (id varchar(20) primary key, name varchar(20))")
# 继续执行一条 SQL 语句，插入一条记录
    curd.execute(r"insert into user (id, name) values ('1', 'Michael')")
except sqlite3.OperationalError, err:
    print err
    if str(err).find("readonly") != -1:
        print "You don't have permission to write this file."
    exit(-1)

# 通过 rowcount 获得插入的行数
print curd.rowcount

# 关闭 Cursor
curd.close()

# 提交事务，使修改生效；在此之前 .db 文件不被修改
cnct.commit()

# 关闭 Connection
cnct.close()
