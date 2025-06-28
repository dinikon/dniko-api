# libs/cors.py
from typing import Any, Dict, Iterable, Sequence

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send


class PrefixCORSMiddleware:
    """CORSMiddleware filtered by path prefix."""

    def __init__(self, app: ASGIApp, prefix: str, **cors_kwargs: Any) -> None:
        self.prefix = prefix.rstrip("/") or "/"
        self.cors = CORSMiddleware(app, **cors_kwargs)
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        path = scope.get("path", "")
        if scope.get("type") == "http" and path.startswith(self.prefix):
            await self.cors(scope, receive, send)
        else:
            await self.app(scope, receive, send)


DEFAULT_METHODS: Sequence[str] = ("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")
            self.router: APIRouter | None = None

        self.router = target

    def include_in(self, parent: FastAPI) -> None:
        """Include router with path-specific CORS middleware."""
        if self.router is None:
            parent.add_middleware(CORSMiddleware, **self._opts)
            return

        parent.include_router(self.router)
        parent.add_middleware(PrefixCORSMiddleware, prefix=self.prefix, **self._opts)
def _normalize(opts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Заполняем опции значениями по умолчанию,
    чтобы не писать их каждый раз.
    """
    return {
        "allow_methods": opts.pop("allow_methods", DEFAULT_METHODS),
        "allow_headers": opts.pop("allow_headers", DEFAULT_HEADERS),
        "allow_origins": opts.pop("allow_origins", ["*"]),
        **opts,
    }


class CORS:
    """
    >>> from libs.cors import CORS
    >>> cors = CORS(router, allow_origins=["https://example.com"])
    >>> cors.mount_to(app)   # или app.mount(cors.prefix, cors.app)
    """

    def __init__(self, target: APIRouter | FastAPI, **cors_kwargs: Any) -> None:
        self._opts = _normalize(cors_kwargs)

        # Если нам дали целый FastAPI-app — просто вешаем middleware
        if isinstance(target, FastAPI):
            target.add_middleware(CORSMiddleware, **self._opts)
            self.app: FastAPI = target
            # fallback: пусть монтируют вручную
            self.prefix = "/"
            return

        # Если APIRouter — оборачиваем в sub-app
        if not isinstance(target, APIRouter):
            raise TypeError("CORS target must be FastAPI or APIRouter")

        self.prefix = target.prefix or "/"
        sub = FastAPI(
            title=f"CORS-wrapped {self.prefix}", docs_url=None, redoc_url=None
        )
        sub.add_middleware(CORSMiddleware, **self._opts)
        sub.include_router(target)
        self.app = sub

    # sugar
    def mount_to(self, parent: FastAPI) -> None:
        """
        parent.mount("/prefix", self.app) одним вызовом.
        """
        parent.mount(self.prefix, self.app)
