from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Request, Depends
from starlette.responses import JSONResponse

from dependencies.container import Container
from services.ml import MLService
from schemas.request_model import Request as UserRequest

ml_router = APIRouter(prefix="ml/")


@ml_router.post("/generate")
@inject
async def ml_generate_answer(
        user_request: UserRequest,
        ml_service: MLService = Depends(Provide[Container.ml_service]),
):
    text, coefficient = ml_service.generate(**user_request.model_dump())
    ml_service.create_log(**user_request.model_dump(),
                          generated_text=text,
                          model_coefficient=coefficient)

    return JSONResponse({
        "id": user_request.id,
        "text": text,
        "coefficient": coefficient
    })
