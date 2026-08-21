from sqlalchemy import Column, Integer, String, TIMESTAMP ,ForeignKey ,Float
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from Database.database import Base

class User(Base) :

    __tablename__ = "users"

    id = Column(Integer ,nullable=False ,primary_key=True)
    email = Column(String , nullable=False)
    pwd = Column(String , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    expenses = relationship("Expense", back_populates="owner")

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String , nullable=False)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="expenses")

