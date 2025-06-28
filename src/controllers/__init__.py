from fastapi import APIRouter

from .constants import API_VERSION

from .ui import router as ui_router
from .vendors import router as vendors_router
from .public_api import router as public_api_router
from .platform import router as platform_router
from .system import router as system_router

router = APIRouter(prefix=f"/api/{API_VERSION}")

router.include_router(system_router)
router.include_router(ui_router)
router.include_router(vendors_router)
router.include_router(public_api_router)
router.include_router(platform_router)
