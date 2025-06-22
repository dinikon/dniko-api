from dniko_app import DNikoApp


def init_app(app: DNikoApp):

    from controllers.console import router as console_app_router

    app.include_router(console_app_router)
