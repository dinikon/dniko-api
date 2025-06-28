from libs.cors import CORS
from src.dniko_app import DNikoApp
from fastapi.middleware.cors import CORSMiddleware


def init_app(app: DNikoApp):

    from controllers.console import router as console_app_router

    CORS(
        console_app_router,
        allow_origins=["*"],
        allow_credentials=True,
        allow_headers=["Content-Type", "Authorization", "X-App-Code"],
        expose_headers=["X-Version", "X-Env"],
        allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    ).mount_to(app)
