from typing import Annotated
from fastapi import Depends, FastAPI,Request,HTTPException
from fastapi.exceptions import ResponseValidationError
import jwt
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

async def auth_jwt(request:Request):
    token = request.headers.get("auth-token")
    if not token:
        raise HTTPException(status_code=401, detail="Token ausente")
    try:
        token_checked = jwt.decode(token, secret_key, algorithms=["HS256"])
        return token_checked
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")