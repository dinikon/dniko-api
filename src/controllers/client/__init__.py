from fastapi import APIRouter

from . import auth, orders, profile

router = APIRouter(prefix="/client", tags=["client"])

router.include_router(auth.router)
router.include_router(orders.router)
router.include_router(profile.router)
