from fastapi import APIRouter
import bcrypt
from app.models.user import User
from fastapi.exceptions import HTTPException
from tortoise.exceptions import IntegrityError
from fastapi import status
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv("SECRET_KEY")


# jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
# {'some': 'payload'}

router = APIRouter(prefix="/user")

@router.get("/all")
async def get_all_users():
    users = await User.all()
    return {"users":users}
    


@router.post(
    "/create",
    summary="Criação de usuário",
    description="Cria um novo usuário com nome, e-mail e senha fornecidos. Obs: essa senha é um hash então não será possível visualisa-la no banco de dados!")
async def create_user(name,email,password):
    try:
        user = await User.filter(email=email)
        if len(user) == 0:
            hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            currentUser = await User.create(name=name,email=email,password=hashed)
            
            
            return {"User created sucessfuly!"}
        else:
            return {"email already in use!"}
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user already exists!"
        )
    
    
@router.get(
    "/login",
    summary="Login de usuário",
    description="Conecta-se à aplicação retornando um token jwt para poder utilizar as funções da aplicação"
    )
async def login(email:str,password:str):
   
    user = await User.filter(email=email).first()
    print(user.id,user.name)
    
    
    if user != None:
        if bcrypt.checkpw(password.encode("utf-8"), user.password):
            encoded_jwt = jwt.encode({
                "user_id": user.id,
                "user_name":user.name
                }, secret_key , algorithm="HS256")
            
            return {"message": "Login successfully!", "access_token": encoded_jwt}
        else:
            return {"wrong password!"}
    else:
        return {"email incorreto ou enexistente"}
    
