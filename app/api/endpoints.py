
from fastapi import APIRouter, Depends, Request, HTTPException, status, Response
from app.services.market_data import get_market_data
from app.services.analysis import analyze_market_data
from app.core.security import get_api_key, limiter
from app.core.logger import logger

router = APIRouter()

# In-memory session tracking for API usage
# Maps API Key -> Request Count
session_usage = {}

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str, 
    download: bool = False,
    api_key: str = Depends(get_api_key)
):
    """
    Analyzes market data for a specific sector.
    
    - **sector**: The industry sector to analyze.
    - **download**: Set to true to download as .md file.
    """
    # Track usage (Session Tracking)
    if api_key not in session_usage:
        session_usage[api_key] = 0
    session_usage[api_key] += 1
    logger.info(f"Request from user {api_key}. Total requests: {session_usage[api_key]}")

    try:
        # 1. Collect Data
        data = get_market_data(sector)
        
        # 2. Analyze Data
        report = analyze_market_data(sector, data)
        
        if download:
            return Response(
                content=report,
                media_type="text/markdown",
                headers={"Content-Disposition": f"attachment; filename={sector}_report.md"}
            )

        return {
            "sector": sector,
            "session_usage_count": session_usage[api_key],
            "report": report
        }
    except ValueError as ve:
        # Client side error (e.g. missing config)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        # Server side error (External API failure)
        logger.critical(f"Internal Server Error: {e}")
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Service unavailable. Please try again later.")
