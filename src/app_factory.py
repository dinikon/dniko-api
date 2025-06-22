from src.dniko_app import DNikoApp


def create_fast_api_app():
    d_niko_app = DNikoApp()
    return d_niko_app


def create_app() -> DNikoApp:
    app = create_fast_api_app()
    return app
