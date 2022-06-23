## ----------------------------
## Login test code
## ----------------------------
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import pandas as pd

admin_name = "root"
admin_pwd = "qwer1234"
db_host = "localhost"
db_name = "moongit_login"

conn = pymysql.connect(host=db_host, user=admin_name, password=admin_pwd, db=db_name, charset="utf8")
cursor = conn.cursor()

sql = "select * from userList"

temp = conn.cursor()
temp.execute(sql)
result = temp.fetchall()
print(len(result))
for i in result:
    print(i)

conn.close()
