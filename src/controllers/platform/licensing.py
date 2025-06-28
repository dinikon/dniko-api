from fastapi import APIRouter

router = APIRouter()


@router.get("/license/status")
async def license_status():
    return {"status": "ok"}
