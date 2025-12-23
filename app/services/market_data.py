
from duckduckgo_search import DDGS
from app.core.logger import logger

def get_market_data(sector: str) -> str:
    """
    Searches for current market data and trends for a specific sector in India.
    Attempts to use DuckDuckGo. If it fails, returns a fallback message to allow AI analysis to proceed with general knowledge.
    """
    logger.info(f"Fetching market data for sector: {sector}")
    query = f"current market trends trade opportunities {sector} sector India {2024}"
    results = []
    
    try:
        with DDGS() as ddgs:
            # Get news and general search results
            search_results = list(ddgs.text(query, max_results=5))
            if not search_results:
                logger.warning(f"No results found for sector: {sector}")
                # Don't return empty, return a hint for AI to use general knowledge
                return f"Note: No specific recent news found for {sector}. Please analyze based on general market knowledge."
                
            for r in search_results:
                results.append(f"Title: {r.get('title')}\nLink: {r.get('href')}\nSnippet: {r.get('body')}\n")
                
        logger.info(f"Successfully retrieved {len(results)} search results for {sector}")
        return "\n---\n".join(results)

    except Exception as e:
        logger.error(f"Error fetching data from DuckDuckGo: {e}")
        # Fallback: Return a message indicating data fetch failure, asking AI to use internal knowledge.
        # This prevents 503 errors and meets the 'Graceful error handling' requirement.
        return (
            f"SYSTEM NOTE: Real-time market data collection failed due to external API connectivity issues ({str(e)}). "
            f"Please provide an analysis of the '{sector}' sector in India based on your internal training data up to 2024."
        )
