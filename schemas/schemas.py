from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    pwd: str

class UserResponse(BaseModel):
    id: int
    class Config:
        from_attributes = True


class ExpenseCreate(BaseModel):
    title: str
    description: str
    price: float

class ExpenseResponse(ExpenseCreate):
    id: int
    class Config:
        from_attributes = True



class Token(BaseModel) :
    access_token : str
    token_type  : str

class TokenData(BaseModel):
    id : Optional[int] = None