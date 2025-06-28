from fastapi import APIRouter

router = APIRouter(prefix="/public", tags=["public"])


@router.post("/webhook")
async def public_webhook():
    return {"message": "webhook received"}
