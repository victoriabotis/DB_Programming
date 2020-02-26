import pymysql
from secrets import host, user, password
import datetime

db = pymysql.connect(host, user, password, "default")
with db.cursor() as c:
    c.execute(
        "SELECT tstamp, cnt FROM bikesharing WHERE tstamp BETWEEN %s AND %s",
        (datetime.datetime(2016, 1, 1, 0), datetime.datetime(2016, 1, 1, 5)),
    )
    print(c.description)
    print(f"Column names: {[d[0] for d in c.description]}") # ne da numele coloanelor unui tabel
    print(c.fetchone())  # first row
    print(c.fetchall())  # remaining rows
    print(f"Got {c.rowcount} rows")

db.close()
