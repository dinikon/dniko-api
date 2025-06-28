from fastapi import APIRouter

from .plans import router as plans_router
from .invoices import router as invoices_router

router = APIRouter(prefix="/admin", tags=["platform_admin"])

router.include_router(plans_router)
router.include_router(invoices_router)
