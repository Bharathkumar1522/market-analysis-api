# Market Analysis API 📊

## 📖 Project Overview
This project is a high-performance **FastAPI service** designed to analyze market data and generate trade opportunity insights for specific sectors in India. It leverages **Google's Gemini AI** for intelligent market analysis and **DuckDuckGo** for real-time data collection, providing structured reports in Markdown format.

## ✨ Features
*   **Sector Analysis**: Deep dive into specific industries (e.g., Pharmaceuticals, Technology).
*   **AI-Powered Insights**: Uses Google Gemini LLM to synthesize data and predict trends.
*   **Real-time Data**: Fetches the latest market news and trade info via DuckDuckGo.
*   **Secure**: Implements API Key authentication and Rate Limiting (`5 req/min`).
*   **Efficiency**: In-memory session tracking and optimized async endpoints.
*   **Downloadable Reports**: Option to download analysis directly as a `.md` file.

## 🛠️ Technical Stack
*   **Framework**: FastAPI
*   **Server**: Uvicorn
*   **AI Model**: Google Gemini (`gemini-1.5-flash`)
*   **Search**: DuckDuckGo Search
*   **Security**: SlowAPI (Rate Limiting), API Key Auth

---

## 🚀 Setup Instructions

### Prerequisites
*   Python 3.9 or higher
*   A Google Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))

### 1. Clone the Repository
```bash
git clone https://github.com/Bharathkumar1522/market-analysis-api.git
cd market-analysis-api
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```bash
# Windows
python -m venv venv
venv/Scripts/activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration (.env)
Create a `.env` file in the root directory and add your keys. You can use the template below:

```ini
# .env
GEMINI_API_KEY=your_gemini_api_key_here
API_KEY=your_secret_access_token
```

---

## 🏃 Running the Application

Start the server using Uvicorn:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://localhost:8000`

### 📚 API Documentation
Interactive Swagger UI documentation is available at:
*   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
*   **Deployed Docs**: [https://market-analysis-api-j5k6.onrender.com/docs](https://market-analysis-api-j5k6.onrender.com/docs)   


#### ⚡ Endpoint Cheatsheet

| Method | Endpoint | Query Params | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/analyze/{sector}` | `download=true` (optional) | Returns analysis JSON or downloads `.md` report |
| `GET` | `/docs` | - | API Documentation |
| `GET` | `/health` | - | Health check |


---

## 🧪 Testing (Deployed Version)

If you are testing the API on the **deployed environment**, please use the following credentials to authenticate your requests:

*   **Header Name**: `X-API-Key`
*   **API Key**: `market-analysis-eval-key-2025`

### Sample Request (cURL)
```bash
curl -X 'GET' \
  'https://market-analysis-api-j5k6.onrender.com/analyze/agriculture' \
  -H 'accept: application/json' \
  -H 'X-API-Key: market-analysis-eval-key-2025'
```

---

## 📂 Project Structure
```
fastapi-market-analysis/
├── app/
│   ├── api/            # API Route definitions
│   ├── core/           # Config, Security, Logging
│   ├── services/       # Business Logic (AI & Search)
│   └── main.py         # App entry point
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
