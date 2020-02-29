from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
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

rows = s.query(Student).all()
print(rows)
for row in rows:
    print(row)

print("-------")
total = s.query(Student).count()
print(f"Total students: {total}")

print("-------")
query_result1 = s.query(Student).filter(Student.first_name == "Jasmin")
print(query_result1)
for q in query_result1:
    print(q)

print("-------")
query_result2 = s.query(Student).filter(Student.id >=2, Student.first_name.like("Bre%"))
print(query_result2)
for q in query_result2:
    print(q)

print("-------")
query_result3 = s.query(func.max(Student.id))
print(query_result3)
for q in query_result3:
    print(q)

print("--------")
#Get student to update
query_result4 = s.query(Student).filter(Student.first_name == "Jasmin").first()
print(query_result4)

#Set new last name

query_result4.last_name = "Popescu"
print(query_result4)

s.commit()

# Update multiple Students

query_result5 = s.query(Student).filter(Student.first_name == "John")
for q in query_result5:
    query_result5.last_name = "John"

s.commit()
