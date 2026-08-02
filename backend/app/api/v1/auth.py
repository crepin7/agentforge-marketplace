"""Stub auth."""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class TokenRequest(BaseModel):
    email: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/token", response_model=TokenResponse)
async def issue_token(req: TokenRequest) -> TokenResponse:
    return TokenResponse(access_token=f"dev-{req.email}")
