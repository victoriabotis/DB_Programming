from sqlalchemy import create_engine
from models import Base, Student
from secrets import host, user, password

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(
        user=user, password=password, host=host, db="default"
    )
)

Base.metadata.create_all(eng)
