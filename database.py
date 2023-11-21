from sqlalchemy import ForeignKey, Column, create_engine, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pydantic import ValidationError

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_str = "sqlite:///" + os.path.join(BASE_DIR, "Users.db")

Base = declarative_base()
engin = create_engine(connection_str, echo=True)
Session = sessionmaker(bind=engin)
session = Session()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    mobile = Column(Integer())

    def __repr__(self):
        return f"{self.name} {self.mobile}"


def get_all_users():
    return session.query(Users).all()

def create_student():
    user = {
        "id" : "asd",
        "name" : "Mayu Kumbha",
        "mobile" : 9925799009
    }
    from models import User
    from exceptions import InvalidMobileError

    try:
        User.model_validate(user)
        # print(user.model_dump())
        new_user = Users(user)
        session.add(new_user)
        session.commit()
        return True
    except InvalidMobileError as e:
        print(repr(e))
    except ValidationError as e :
        print("valid")
        print(repr(e))
    except ValueError as e :
        print("value")
        print(repr(e))