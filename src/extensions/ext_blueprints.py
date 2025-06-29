from src.controllers import router as api_router


def init_app(app):
    app.include_router(api_router)
