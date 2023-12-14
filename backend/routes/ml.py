from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from services.ml import generate
from models.request_model import Request as UserRequest

ml_router = APIRouter(prefix="ml/")


@ml_router.post("/generate")
async def ml_generate_answer(
        request: Request,
        user_request: UserRequest
):
    text, coefficient = generate(**user_request.model_dump())
    return JSONResponse({
        "id": user_request.id,
        "text": text,
        "coefficient": coefficient
    })
