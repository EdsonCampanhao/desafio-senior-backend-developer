from fastapi import APIRouter



router = APIRouter(prefix="/health")

@router.get(
    "",
    summary="teste de saúde",
    description="roda um teste simples no servidor para checar se está rodando"
    )
async def health_checker():
    return {"status": "ok"}