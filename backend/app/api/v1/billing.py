"""Endpoints billing (Stripe)."""
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import settings

router = APIRouter()


class CheckoutRequest(BaseModel):
    plan: str


@router.post("/checkout")
async def create_checkout_session(req: CheckoutRequest) -> dict:
    return {
        "checkout_url": f"https://checkout.stripe.com/c/test/{req.plan}",
        "mode": "sandbox",
        "price_id": settings.stripe_price_all_access,
    }


@router.post("/webhook")
async def stripe_webhook(payload: dict) -> dict:
    return {"received": True}
