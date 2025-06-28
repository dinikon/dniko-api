from fastapi import APIRouter

router = APIRouter()

@router.get('/profile')
async def profile_info():
    return {"profile": "info"}
