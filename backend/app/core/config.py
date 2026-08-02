"""Settings via pydantic-settings."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "AgentForge"
    environment: str = "development"
    debug: bool = True

    database_url: str = "postgresql+asyncpg://forge:forge@localhost:5432/agentforge"
    redis_url: str = "redis://localhost:6379/0"

    openai_api_key: str = ""
    anthropic_api_key: str = ""

    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_all_access: str = "price_xxx"

    jwt_secret: str = "change-me-in-prod"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60 * 24 * 7

    cors_origins: list[str] = ["http://localhost:3000"]
    creator_share_bps: int = 7000


settings = Settings()
