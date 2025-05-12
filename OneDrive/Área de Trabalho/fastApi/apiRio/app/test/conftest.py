import pytest_asyncio
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from app.db.dataBase import db
from tortoise.contrib.test import finalizer

@pytest_asyncio.fixture(scope="module", autouse=True)
async def setup_db():
    
    yield
    
