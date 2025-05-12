from fastapi import APIRouter,Depends,HTTPException,Header,status
from app.models.documents import Documents
from app.models.typeOfDocument import typeOfDocuments 
from app.models.user import User
from app.controllers.auth import auth_jwt


router = APIRouter(prefix="/documents")

@router.post(
    "/create/{user_id}/{typeOfDocument_id}",
    summary="cadastro de documento",
    description="Cadastra um novo documento para o usuário!")
async def register_document(
    issuingBody,
    dateOfIssue,
    registrationNumber: int,
    user_id: int,
    typeOfDocument_id: int,
    auth_token:str | None = Header(None),
    checkedToken:str = Depends(auth_jwt)):
    
    if checkedToken["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="operation not permitted for this user!")
    
    try:
        check = await Documents.filter(user_id=user_id,typeOfDocument_id=typeOfDocument_id).first()
        
        if check != None :
            return {"document already registered!"}
        else:
            await Documents.create(
                issuingBody=issuingBody,
                dateOfIssue=dateOfIssue,
                registrationNumber=registrationNumber,
                typeOfDocument_id=typeOfDocument_id,
                user_id=user_id
                )
            
        return {"document registered sucessfuly!"}
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="bad request!"
        )
   
@router.get(
    "/getAll/{user_id}",
    summary="visualisa todos os usuários",
    description="roda um querie para visualizar os usuários cadastrados!"
    )
async def get_all(
    user_id:int,
    auth_token:str | None = Header(None),
    checkedToken:str = Depends(auth_jwt)):
    
    if checkedToken["user_id"] != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="operation not permitted for this user!"
        )
    
    documents=await Documents.filter(user_id=user_id)
    userName=await User.filter(id=user_id) 
    
    return {f"documents of {userName[0].name}":documents}

@router.post(
    "/create_type_of",
    summary="Criação de tipo de documento",
    description="Cria um novo tipo de documento utilizado para cadastrar novos documentos! tentar cadastrar um documento de um tipo que não exista para um usuário retornará erro!")
async def create_type_of(name: str):
    try:
        check = await typeOfDocuments.filter(name=name).first()
        
        if check != None:
            return {"type of document already registered!"}
        else:
            await typeOfDocuments.create(name=name)
            return {"type of document registered sucessfuly!"}
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user already exists!"
        )