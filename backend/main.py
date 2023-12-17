from fastapi import FastAPI, HTTPException

from dependencies.container import Container
from routes.ml import ml_router


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(ml_router)
    return app


app = create_app()


@app.get("/")
async def root():
    return HTTPException(404)

