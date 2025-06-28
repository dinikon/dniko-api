from fastapi import APIRouter

router = APIRouter(prefix="/console", tags=["console"])

from . import ping
