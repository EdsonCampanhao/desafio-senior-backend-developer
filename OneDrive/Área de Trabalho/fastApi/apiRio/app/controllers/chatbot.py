from fastapi import APIRouter,Header,Depends
from app.controllers.bilheteUnico import check_amount
from app.controllers.auth import auth_jwt

router = APIRouter(prefix="/chatBot")

@router.get(
    "/ask/{user_id}",
    summary="Criação de tipo de documento",
    description="simulação de um chat bot para as perguntas : 'Saldo do bilhete único', 'Quais linhas de ônibus passam no município', '2º via do iptu' ")
async def ask(
    user_id:int,
    ask:str,
    auth_token:str | None = Header(None),
    checkedToken:str = Depends(auth_jwt)):
    try:
        match ask:
            case "Saldo do bilhete único":
                return await check_amount(user_id)
            case "Quais linhas de ônibus passam no município":
                return {"Você pode conhecer mais as redes que compõe o nosso municipio em 'https://www.rio.rj.gov.br/dlstatic/10112/4553199/4116432/LinhasMunicipais_16214.pdf'"}
            case "2º via do iptu":
                return {"você pode encontrar está e outras funcionalidades sobre o iptu no nosso site 'https://carioca.rio/tema/iptu'"}

    
    
    except:
        return "something went wrong!"