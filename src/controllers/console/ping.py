from controllers.console import router


@router.get("/ping")
async def ping():
    return "pong"
