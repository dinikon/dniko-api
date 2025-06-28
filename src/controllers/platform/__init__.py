from fastapi import APIRouter

from .licensing import router as licensing_router
from .billing import router as billing_router
from .admin import router as admin_router
from .webhook_receiver import router as webhook_router

router = APIRouter(prefix="/platform", tags=["platform"])

router.include_router(licensing_router)
router.include_router(billing_router)
router.include_router(admin_router)
router.include_router(webhook_router)
