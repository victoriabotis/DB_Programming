from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base() # functie care ne intoarce clasa Base

class Student(Base): # clasa declarativa (doar listam atributele)
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    
    def __str__(self):
        return f"<Student #{self.id} {self.first_name} {self.last_name}>"

class Locker(Base):
    __tablename__= "lockers"
    number = Column(Integer, primary_key=True) 
    student = Column(Integer, ForeignKey(Student.id),primary_key=True) # nu permite duplicate
    
    def __str__(self):
        return f"<Locker {self.number}: {self.student}>"
    
class Address(Base):
    __tablename__= "address" 
    student = Column(Integer, ForeignKey(Student.id),primary_key=True) 
    street_name = Column(String(255))
    number = Column(Integer)
    city = Column(String(255))

    def __str__(self):
        return f"<{self.student}> address is : Street: {self.street_name}, No. {self.number}, City: {self.city}"

class Grades(Base):
    __tablename__= "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student = Column(Integer, ForeignKey(Student.id))
    grade = Column(Integer)
    date_created = Column(DateTime)

    def __str__(self):
        return f"<{self.student}> grade {self.grade} / {self.date_created}"