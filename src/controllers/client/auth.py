from fastapi import APIRouter

router = APIRouter()

@router.post('/login')
async def login():
    return {"status": "logged in"}

@router.post('/refresh')
async def refresh():
    return {"status": "refreshed"}
