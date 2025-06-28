from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/ping")
async def ping():
    return {"status": "ok"}


@router.get("/readiness")
async def readiness_probe():
    return {"status": "ready"}


@router.get("/liveness")
async def liveness_probe():
    return {"status": "alive"}


@router.get("/metrics")
async def metrics():
    return {"metrics": "placeholder"}
