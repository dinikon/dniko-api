from fastapi import APIRouter

router = APIRouter(prefix="/console", tags=["console"])

@router.get("/dashboard")
async def dashboard_example():
    return {"message": "console dashboard"}
