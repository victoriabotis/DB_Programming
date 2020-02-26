import pymysql
from secrets import host, user, password
from datetime import datetime

db = pymysql.connect(host, user, password, "default")

with db.cursor() as c:
    c._defer_warnings = True
    c.execute("""
    CREATE TABLE IF NOT EXISTS `bikesharing` 
    (
        tstamp TIMESTAMP, 
        cnt INTEGER, 
        temperature DECIMAL(5, 2),
        temperatute_feels DECIMAL(5, 2),
        humidity DECIMAL(4,1),
        wind_speed DECIMAL(5, 2),
        weather_code INTEGER,
        is_holiday BOOLEAN,
        is_weekend BOOLEAN,
        season INTEGER
    );""")
    print(c.execute("SELECT * FROM `bikesharing`"))
    c.execute("DELETE FROM `bikesharing`")

    insertStatement = """INSERT INTO `bikesharing` (tstamp, cnt, temperature, temperatute_feels, humidity, wind_speed, 
                                                    weather_code, is_holiday, is_weekend, season) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""   

    with open("/Users/victoriabotis/Documents/DB_Programming/pymysql-1/london-bikes.csv", "r") as f:
        count = 0
        for line in f.readlines()[1:]:
            count = count + 1
            info = line.split(",")
            info[0] = datetime.strptime(info[0], "%Y-%m-%d %H:%M:%S")
            #print(info)
            c.execute(insertStatement, info)
            if count % 100 == 0:
                db.commit()
    db.commit()
db.close()
