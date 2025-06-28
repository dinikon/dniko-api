from controllers.console import router as console_router


def init_app(app):
    app.include_router(console_router)
