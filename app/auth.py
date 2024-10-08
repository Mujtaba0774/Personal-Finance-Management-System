from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .crud import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):   
    user = get_user_by_username("dummy_user")
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
