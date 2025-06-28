from fastapi import APIRouter

from .bitrix import router as bitrix_router
from .dify import router as dify_router
from .payments import router as payments_router
from .ca import router as ca_router

router = APIRouter(prefix="/vendors", tags=["vendors"])

router.include_router(bitrix_router)
router.include_router(dify_router)
router.include_router(payments_router)
router.include_router(ca_router)
