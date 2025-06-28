from fastapi import APIRouter

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("/example")
async def payments_example():
    return {"message": "payments placeholder"}
