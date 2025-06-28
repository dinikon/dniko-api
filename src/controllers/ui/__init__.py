from fastapi import APIRouter

router = APIRouter(prefix="/ui", tags=["ui"])


@router.get("/dashboard")
async def dashboard_example():
    return {"message": "ui dashboard"}
