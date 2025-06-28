from fastapi import APIRouter

router = APIRouter(prefix="/ca", tags=["ca"])


@router.get("/example")
async def ca_example():
    return {"message": "ca placeholder"}
