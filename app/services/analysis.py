
import google.generativeai as genai
from app.core.config import settings
from app.core.logger import logger

# Configure Gemini
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)

def analyze_market_data(sector: str, market_data: str) -> str:
    """
    Uses Gemini API to analyze market data and generate a structured markdown report.
    """
    if not settings.GEMINI_API_KEY:
        logger.error("GEMINI_API_KEY missing")
        raise ValueError("GEMINI_API_KEY not found. Analysis cannot be performed.")

    if not market_data:
        logger.warning(f"Insufficient data for analysis for sector: {sector}")
        return f"No sufficient data found for sector '{sector}' to perform analysis."

    logger.info(f"Starting Gemini analysis for sector: {sector}")

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        You are a Trade Analyst Expert. Analyze the following market data for the '{sector}' sector in India and provide a structured report on trade opportunities.
        
        Market Data:
        {market_data}
        
        Required Report Format (Markdown):
        # Trade Opportunities Report: {sector.capitalize()}
        
        ## 1. Market Overview
        - Current status and key trends.
        
        ## 2. Key Trade Opportunities
        - Import/Export potential.
        - Emerging niches.
        
        ## 3. Risks and Challenges
        - Regulatory hurdles or market barriers.
        
        ## 4. Conclusion & Recommendations
        
        ## 5. Sources
        - List the titles/links provided in the data.
        """
        
        response = model.generate_content(prompt)
        logger.info("Gemini analysis completed successfully")
        return response.text
        
    except Exception as e:
        logger.error(f"Error during AI analysis: {str(e)}")
        logger.warning(f"Returning fallback report for {sector}")
        
        # Fallback Report to ensure the API works even if Gemini fails (e.g. network/quota issues)
        return f"""
# Trade Opportunities Report: {sector.capitalize()} (Fallback)

> **Note**: The AI analysis service is currently unavailable. This is a generated placeholder report based on the requested sector.

## 1. Market Overview
The **{sector}** sector in India is currently witnessing significant activity. While real-time AI analysis is temporarily unavailable, this sector generally plays a pivotal role in the country's economy.

## 2. Key Trade Opportunities
- **Exports**: High potential in international markets.
- **Domestic Growth**: Increasing demand within tier-2 and tier-3 cities.

## 3. Risks and Challenges
- **Regulatory**: Compliance with evolving government standards.
- **Global Factors**: Supply chain disruptions and currency fluctuations.

## 4. Conclusion
Investors and businesses are advised to monitor official government announcements and trade bodies for the most accurate and up-to-date specific opportunities in {sector}.

## 5. Sources
- *Data processing fell back to internal templates due to: {str(e)}*
- *Refer to the snippet provided in the 'market_data' section if available.*
"""
