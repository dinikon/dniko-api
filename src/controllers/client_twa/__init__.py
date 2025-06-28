from fastapi import APIRouter

router = APIRouter(prefix="/client/twa", tags=["client_twa"])

@router.post('/callback')
async def twa_callback():
    return {"twa": "callback"}
