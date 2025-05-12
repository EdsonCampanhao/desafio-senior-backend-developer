from fastapi import APIRouter,Header,Depends
from app.models.bilheteUnico import BilheteUnico
from app.models.user import User
from app.controllers.auth import auth_jwt

router = APIRouter(prefix="/bilheteUnico")


@router.get(
    "/amount/{user_id}",
    summary="Checa saldo!",
    description="visualisa saldo restante no bilhete único!")
async def check_amount(
    user_id:int,
    auth_token:str | None = Header(None),
    checkedToken:str = Depends(auth_jwt)):
    try:
        check= await BilheteUnico.filter(user_id=user_id).first()
        if check != None:
            return {"the user has a balance of":check[0].amount}
        else:
            return {"the user does not have a bilhete unico yet!"}
        
    except:
        return {"something went wrong!"}
    
@router.post(
    "/create",
    summary="CriaB.u",
    description="Cadastra um bilhete único para o usuário!")
async def create_bilhete(
    user_id:int,
    auth_token:str | None = Header(None),
    checkedToken:str = Depends(auth_jwt)):
    try:
        check= await BilheteUnico.filter(user_id=user_id)
        if len(check)>0:
            return {"the user already have a bilhete unico!"}
        else:
            await BilheteUnico.create(user_id=user_id)
            return {"bilhete unico created sucessfully!"}
    except:
        return {"something went wrong!"}
    
@router.post(
    "/cash_in/{user_id}",
    summary="cobra saldo",
    description="Remove quantia do bilhete único! caso valor seja maior do que o usuário tem retornara um erro")
async def cash_in(user_id:int,value:float):
    try:
        check= await BilheteUnico.filter(user_id=user_id)
        if len(check)==0:
            return {"the user does not have a bilhete unico yet!!"}
        elif check[0].amount < value:
            return {"the user has not enougth credit!"}
        else:
            newAmount=float(check[0].amount)-value
            await BilheteUnico.filter(user_id=user_id).update(amount=newAmount)
            return {"cash-in done sucessfuly! remaining value":newAmount}
    except:
        return {"something went wrong!"}
    
@router.post(
    "/recharge/{user_id}",
    summary="carrega B.U",
    description="carrega determinada quantia de dinheiro")
async def recharge(user_id:int,value:float):
    
        check= await BilheteUnico.filter(user_id=user_id)
        if len(check)==0:
            return {"the user does not have a bilhete unico yet!!"}
        else:
            newAmount=float(check[0].amount)+value
            await BilheteUnico.filter(user_id=user_id).update(amount=newAmount)
            return {"recharge done sucessfuly! new value":newAmount}
   
    
