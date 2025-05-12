import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
from app.db.dataBase import db
from tortoise import Tortoise
from app.models.user import User
from app.controllers import user
from app.controllers import documents
from app.controllers import bilheteUnico
from app.controllers import chatbot
from app.controllers import healfChecker



app = FastAPI()
app.include_router(user.router)
app.include_router(documents.router)
app.include_router(bilheteUnico.router)
app.include_router(chatbot.router)
app.include_router(healfChecker.router)

async def check_connection():
    try:
        # Faz uma consulta simples para verificar a conexão
        await Tortoise.get_connection('default').execute_query("SELECT 1")
        print("Conexão ativa com o banco de dados!")
    except Exception as e:
        print(f"Falha ao conectar ao banco de dados: {e}")
        
@app.on_event("startup")
async def startup():
    dataBase = await db()  # Inicializa a conexão
    await check_connection()
    

   