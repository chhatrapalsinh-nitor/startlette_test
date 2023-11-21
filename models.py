from pydantic import BaseModel, validator
from typing import Optional
from exceptions import InvalidMobileError




class User(BaseModel):
    id: int
    name: str
    mobile : Optional[int]

    @validator("mobile")
    @classmethod
    def mobile_valid(cls, value) :
        letter_count = len([i for i in str(value)])
        if letter_count != 10 :
            raise InvalidMobileError(value= value, message="Mobile numbe should be 10 digits long..")
        return value
        
