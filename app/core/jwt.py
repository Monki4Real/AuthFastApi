from config import settings
from datetime import datetime, timedelta 
import jwt

key = settings.SECRET_KEY

time_exp = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    exp = timedelta(minutes=time_exp) + datetime.now()
    token_data = data.copy()
    token_data ["exp"] = exp
    token = jwt.encode(token_data, key, algorithm='HS256')
    return token



def verify_token(token:str):
    try:
        payload  = jwt.decode(token, key, algorithm='HS256')
        return payload 
    except jwt.InvalidTokenError:
        return None

