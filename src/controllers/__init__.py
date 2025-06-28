from fastapi import APIRouter

from config import d_niko_config
from .constants import API_VERSION

from .console import router as console_router
from .client import router as client_router
from .client_mobile import router as client_mobile_router
from .client_twa import router as client_twa_router
from .vendors import router as vendors_router
from .public_api import router as public_api_router
from .platform import router as platform_router
from .system import router as system_router

router = APIRouter(prefix=f"/api/{d_niko_config.API_VERSION}")

router.include_router(system_router)
router.include_router(console_router)
router.include_router(client_router)
router.include_router(client_mobile_router)
router.include_router(client_twa_router)
router.include_router(vendors_router)
router.include_router(public_api_router)
router.include_router(platform_router)
