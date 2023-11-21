from database import Base, engin, Users, create_student

Base.metadata.create_all(bind=engin)
