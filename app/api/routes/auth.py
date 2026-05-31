from fastapi import APIRouter, Depends
from app.schemas.auth import UserCreate
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['auth']
)


@router.post('/register')
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
    ):
    pass