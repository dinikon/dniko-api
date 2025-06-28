from fastapi import APIRouter

router = APIRouter()


@router.post("/webhook/payment-succeeded")
async def payment_succeeded():
    return {"status": "received"}
