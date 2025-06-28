from fastapi import APIRouter

router = APIRouter()


@router.get("/subscription")
async def subscription_info():
    return {"subscription": "active"}
