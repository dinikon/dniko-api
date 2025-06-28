import logging
import time

from config import d_niko_config
from extensions import ext_blueprints
from src.dniko_app import DNikoApp


def create_fast_api_app():
    d_niko_app = DNikoApp()
    return d_niko_app


def create_app() -> DNikoApp:
    app = create_fast_api_app()
    initialize_extensions(app)
    return app


def initialize_extensions(app: DNikoApp):
    from extensions import (
        ext_blueprints,
    )

    extensions = [
        ext_blueprints,
    ]
    for ext in extensions:
        short_name = ext.__name__.split(".")[-1]
        is_enabled = ext.is_enabled() if hasattr(ext, "is_enabled") else True
        if not is_enabled:
            if d_niko_config.DEBUG:
                logging.info(f"Skipped {short_name}")
            continue

        start_time = time.perf_counter()
        ext.init_app(app)
        end_time = time.perf_counter()
        if d_niko_config.DEBUG:
            logging.info(
                f"Loaded {short_name} ({round((end_time - start_time) * 1000, 2)} ms)"
            )
