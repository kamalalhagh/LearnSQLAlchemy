from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

base_dir = os.getcwd()
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    uid = Column("uid", Integer, primary_key=True)
    firstname = Column("first name", String)
    lastname = Column("last name", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, uid, firstname, lastname, gender, age):
        self.uid = uid
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.uid}) : {self.firstname} {self.lastname}, {self.gender}, {self.age} years old."


class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.uid"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) : {self.description}, Owner(uid): {self.owner}"


engine = create_engine("sqlite:///" + os.path.join(base_dir, "Database.db"), echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
## add data:
# p1 = Person(1234, "firstname", "Lastname", "M", 20)
# t1 = Thing(12, "guitar", p1.uid)
# session.add(p1)
# session.add(t1)
# session.commit()

## get the results:
# result_person = session.query(Person).all()
# result_thing = session.query(Thing).all()
# print(result_person)
# print(result_thing)
