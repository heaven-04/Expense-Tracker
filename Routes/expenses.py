from fastapi import APIRouter , HTTPException, Response , Depends , status
from schemas import schemas
from models import models
from sqlalchemy.orm import Session
from Database.database import get_db
from APP import oauth2
from typing import List


router = APIRouter(prefix="/expenses" , tags=["Expenses"])

@router.get("/",response_model=List[schemas.ExpenseResponse])
def get_expenses(db : Session = Depends(get_db) , get_current_user : int = Depends(oauth2.get_current_user) ):
    expenses = db.query(models.Expense).filter(models.Expense.user_id == get_current_user.id).all()
    if not expenses :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return expenses


@router.post("/add")
def add_expenses(expense : schemas.ExpenseCreate, db : Session = Depends(get_db) , get_current_user : int = Depends(oauth2.get_current_user)):
    new_expense = models.Expense(**expense.model_dump(),user_id=get_current_user.id)
    db.add(new_expense)
    db.commit()
    return Response(status_code=status.HTTP_201_CREATED)



@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_expenses(id: int, db: Session = Depends(get_db),  current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    expense_query = db.query(models.Expense).filter(models.Expense.id == id)
    expense = expense_query.first()
    if expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {id} not found"
        )
    if expense.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )
    expense_query.delete(synchronize_session=False)
    db.commit()
    return  Response(status_code=status.HTTP_204_NO_CONTENT)