from sqlalchemy import (
    create_engine,
    ForeignKey,
    Column,
    String,
    Integer,
    CHAR,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime


url_object = URL.create(
    "mysql",
    username="z",
    password="kZ^hSkn73",  # plain (unescaped) text
    host="localhost",
    database="mydb",
)

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    # p_id = Column("p_id", Integer, Integer_AutoIncrementType="auto", primary_key=True)
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String(50))
    lastname = Column("lastname", String(50))
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return (
            f" ({self.ssn}) {self.firstname} {self.lastname} ({self.gender},{self.age})"
        )


class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("discription", String(50))
    owner = Column("owner", Integer, ForeignKey("people.ssn"))
    date = Column("date", DateTime)

    def __init__(self, tid, discription, owner, date):
        self.tid = tid
        self.description = discription
        self.owner = owner
        self.date = date

    def __repr__(self):
        return f"(self.tid) {self.description} owned by {self.owner}"


engine = create_engine(url_object, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

p0 = Person(120, "Mike", "Smith", "m", 35)
p1 = Person(121, "Anna", "Blue", "f", 40)
p2 = Person(122, "Bob", "Blue", "m", 35)
p3 = Person(123, "Angela", "Cold", "m", 22)

session.add(p0)
session.add(p1)
session.add(p2)
session.add(p3)

session.commit()

t1 = Thing(1, "car", p1.ssn, datetime.now())
t2 = Thing(2, "PS5", p1.ssn, datetime.now())
t3 = Thing(3, "Laptop", p2.ssn, datetime.now())

session.add(t1)
session.add(t2)
session.add(t3)

session.commit()

# results = session.query(Person).all()
# results = session.query(Person).filter(Person.lastname == "Blue")
# results = session.query(Person).filter(Person.firstname.like("%An%"))
# results = session.query(Person).filter(Person.firstname.in_(["Anna", "Mike"]))

results = (
    session.query(Thing, Person)
    .filter(Thing.owner == Person.ssn)
    .filter(Person.firstname == "Anna")
    .all()
)

for r in results:
    print(r)
