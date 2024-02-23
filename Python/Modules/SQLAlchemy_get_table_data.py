from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
from sqlalchemy.ext.automap import automap_base
import pandas as pd

url_object = URL.create(
    "mysql",
    username="",
    password="",  # plain (unescaped) text
    host="",
    database="",
)

engine = create_engine(url_object, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = automap_base()
Base.prepare(engine)

table = Base.classes.table


name = input("Enter name:")

result = (
    session.query(table)
    .filter(table.name == name)
    .order_by(table.timestamp.desc())
    .limit(10)
)

# for i in result:
#     print(i)


def as_dict(obj):
    data = obj.__dict__
    data.pop("_sa_instance_state")
    return data


# add the `as_dict` function to the classes
for c in [table]:
    c.as_dict = as_dict


# e.g return this as a rest-api response
list_dict_result = [r.as_dict() for r in result]

# print(list_dict_result)
# for r in list_dict_result:
#     print(r)


df = pd.DataFrame(list_dict_result)
df = df.reindex(
    columns=[
        "id",
        "name",
    ]
)

df.to_csv("files.txt", sep="\t", index=False, na_rep="None")
