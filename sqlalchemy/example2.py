from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from secrets import host, user, password

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}" #primul parametru este baza de data(mysql) + al doilea conectorul

eng = create_engine(
    CONNECTION_STRING.format(
        user=user, password=password, host=host, db="default"
    )
)

Base.metadata.create_all(eng)

Session = sessionmaker(bind=eng) # tine deschisa conexiunea la baza de date
s = Session() # deschide o conexiune 

s.add_all(
    [
        Student(first_name = "Mike", last_name = "Wazowski"),
        Student(first_name = "Netti", last_name = "Nashe"),
        Student(first_name = "Jasmin", last_name = "Addison"),
        Student(first_name = "Brena", last_name = "Bugdale"),
        Student(first_name = "Theobald", last_name = "Oram")
    ]
)

s.commit()
