from fastapi import APIRouter

router = APIRouter(prefix="/dify", tags=["dify"])


@router.get("/example")
async def dify_example():
    return {"message": "dify placeholder"}
