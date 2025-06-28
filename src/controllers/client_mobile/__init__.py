from fastapi import APIRouter

router = APIRouter(prefix="/client/mobile", tags=["client_mobile"])

@router.get('/ping')
async def mobile_ping():
    return {"mobile": "pong"}
