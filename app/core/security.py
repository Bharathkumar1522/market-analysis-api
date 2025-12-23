
from fastapi import Security, HTTPException, Request
from fastapi.security.api_key import APIKeyHeader
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.core.config import settings

# Rate Limiter Setup
limiter = Limiter(key_func=get_remote_address)

# Simple API Key Auth
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == settings.API_KEY:
        return api_key_header
    # For the sake of this assignment, we can also allow no auth or throw error.
    # The requirements say "Authentication (simple auth/JWT/guest auth - your choice)"
    # We will enforce it but give a default in .env for testing clarity.
    if not settings.API_KEY: # If no key set in env, allow open access (dev mode)
        return "open-access"
        
    raise HTTPException(
        status_code=403,
        detail="Could not validate credentials",
    )
