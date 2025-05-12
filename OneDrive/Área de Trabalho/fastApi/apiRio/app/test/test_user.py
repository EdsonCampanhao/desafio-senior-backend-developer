import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient


  
@pytest.mark.asyncio
async def test_user():
    async with AsyncClient(base_url="http://api:8000") as client:
        response =await  client.post("/user/create", params={
            "name": "test_usuario",
            "email": "testaaaaa@example.com",
            "password": "12345"
        })
    
    assert response.status_code == 200
    assert "user created" in response.text.lower()