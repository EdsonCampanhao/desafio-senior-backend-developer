from tortoise import Tortoise, run_async
from dotenv import load_dotenv
import os
import asyncmy
import asyncio

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
DB_NAME=os.getenv("DB_NAME")
DB_PORT=os.getenv("DB_PORT")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_USER=os.getenv("DB_USER")
DB_HOST=os.getenv("DB_HOST")


async def db():
    # Conexão com o banco de dados MySQL
    await Tortoise.init(config={
            'connections': {
                'default': {
                   'engine': 'tortoise.backends.mysql'  # em vez de asyncmy
,  # Usando o backend asyncmy para MySQL
                    'credentials': {
                        'host': DB_HOST,
                        'port': DB_PORT,  # Porta padrão do MySQL
                        'user':DB_USER ,  # Seu usuário do MySQL
                        'password': DB_PASSWORD,  # Sua senha do MySQL
                        'database': DB_NAME,  # Nome do seu banco de dados
                    }
                },
            },
            'apps': {
                "models": {
                    "models": [
                        "aerich.models",
                        "app.models.bilheteUnico",
                        "app.models.documents",
                        "app.models.typeOfDocument",
                        "app.models.user"
                        ],
                    "default_connection": "default",
            }
            }
        }
    )
    await Tortoise.generate_schemas()
