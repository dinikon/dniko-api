from fastapi import APIRouter

router = APIRouter(prefix="/bitrix", tags=["bitrix"])


@router.get("/example")
async def bitrix_example():
    return {"message": "bitrix placeholder"}
