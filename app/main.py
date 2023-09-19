from fastapi import FastAPI
from app import routes

from app.containers import Container


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container  # type: ignore
    app.include_router(routes.router)
    return app


app = create_app()
