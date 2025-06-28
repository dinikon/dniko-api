from fastapi import APIRouter

router = APIRouter()


@router.get("/plans")
async def list_plans():
    return {"plans": []}
