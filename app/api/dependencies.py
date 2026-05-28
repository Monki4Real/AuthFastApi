from fastapi import Depends, OAuth2PasswordBearer, HTTPException 
from sqlalchemy.orm import Session
from app.core.jwt import verify_token
from app.database import get_db
from app.models import User

oauth2_scheme  = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User: 
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401)
    else:
        user_id = payload['sub']

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=401)
    else:
        return user

