from sqlalchemy.exc import IntegrityError, InvalidRequestError
from models import Base, Student, Locker, Address, Grades
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secrets import host, user, password
from sqlalchemy import desc

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}" 

eng = create_engine(
    CONNECTION_STRING.format(
        user=user, password=password, host=host, db="default"
    )
)

Base.metadata.create_all(eng)

Session = sessionmaker(bind=eng) 
s = Session() 

try:
    s.add_all(
        [
            Locker(number=1, student=4),
            Locker(number=2, student=1), 
            Locker(number=3, student=5), 
            Locker(number=4, student=2), 
            Locker(number=5, student=3),
        ]
    )
    s.commit()
except IntegrityError:
    s.rollback()
    print("Lockers already created!")

try:
    s.add_all(
        [
            Address(student=1, street_name = "Park Lake", number = 2, city = "San Francisco"),
            Address(student=2, street_name = "5th Avenue", number = 102, city = "New York"),
            Address(student=3, street_name = "Addison", number = 5, city = "Chicago"),
            Address(student=4, street_name = "Champs Elisee", number =100, city = "Paris"),
            Address(student=5, street_name = "Las Ramblas", number =165, city = "Barcelona"),
        ]
    )
    s.commit()
except IntegrityError:
    s.rollback()
    print("Addresses already created!")

# s.add_all(
#         [
#             Grades(student=1, grade = 10, date_created = "2019-06-01"),
#             Grades(student=2, grade = 8, date_created = "2019-06-01"),
#             Grades(student=3, grade = 9, date_created = "2019-06-01"),
#             Grades(student=4, grade = 10, date_created = "2019-06-01"),
#             Grades(student=5, grade = 5, date_created = "2019-06-01"),
#             Grades(student=1, grade = 9, date_created = "2019-05-25"),
#             Grades(student=2, grade = 10, date_created = "2019-05-25"),
#             Grades(student=4, grade = 9, date_created = "2019-05-25")
#         ]
#     )
# s.commit()

# s.add_all(
#         [
#             Grades(student=1, grade = 10, date_created = "2019-06-06"),
#             Grades(student=2, grade = 9, date_created = "2019-06-06"),
#             Grades(student=3, grade = 9, date_created = "2019-06-06")
#         ]
#     )
# s.commit()

# rows = s.query(Student, Locker).join(Locker).filter(Locker.number == 4) 
# for row in rows:
#     student, locker = row
#     print(f"Student with locker #{locker.number}: {student}")

# print("-------")
# rows1 = s.query(Student, Address).join(Address).all()
# for row in rows1:
#     student, address = row
#     print(f"{student.last_name} {address}")

# print("-------")
# rows2 = s.query(Student, Locker, Address).join(Locker).join(Address).all()
# for row in rows2:
#     student, locker, address = row
#     print(f"{student} {address} / locker #{locker.number}")

# for student, address in s.query(Student, Address).join(Address).order_by(Student.last_name):
#     print(f"{student.last_name} {address}")

# for student, address in s.query(Student, Address).join(Address).order_by(desc(Student.last_name)):
#     print(f"{student.last_name} {address}")

# for student, address in s.query(Student, Address).join(Address).order_by(desc(Student.last_name)).limit(3):
#     print(f"{student.last_name} {address}")

# student, address = s.query(Student, Address).join(Address).filter(Address.city == "New York").first()
# print(student, address)
# address.city = "Chicago"
# print(student, address)

# s.commit()

# user, locker, address = s.query(Student, Locker, Address).join(Locker).join(Address).filter(Student.id == 1).first()
# print(user)
# s.delete(address)
# s.commit()
# s.delete(locker)
# s.commit()
# s.delete(user)
# s.commit()

# for student, grades in s.query(Student, Grades).join(Grades).all():
#     print(f"{student.last_name} {grades}")

for student in s.query(Student).all():
    print(student)
    for grade in s.query(Grades).filter(Grades.student == student.id):
        print(f"\t {grade}")