import pymysql
from secrets import host, user, password

db = pymysql.connect(host, user, password, "")

with db.cursor() as c:
    c._defer_warnings = True
    c.execute("CREATE SCHEMA IF NOT EXISTS `default` DEFAULT CHARACTER SET utf8;")
db.close()

db = pymysql.connect("127.0.0.1", "root", "", "default")
db.close()
