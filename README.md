# Sentiment Analysis Portfolio

AI-powered sentiment analysis web application built with FastAPI and Streamlit.

## Features

- **AI Model:** Hugging Face sentiment analysis
- **FastAPI Backend:** RESTful API with automatic documentation
- **Streamlit Frontend:** Modern web interface
- **Error Handling:** User-friendly error messages
- **Responsive Design:** Works on all devices

## Tech Stack

- **Backend:** FastAPI, Hugging Face Transformers
- **Frontend:** Streamlit
- **AI Model:** cardiffnlp/twitter-roberta-base-sentiment-latest
- **Language:** Python

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run API: `python -m uvicorn main:app --reload`
4. Run Frontend: `streamlit run app.py`
5. Open browser: `http://localhost:8501`

## API Endpoints

- `GET /` - Health check
- `GET /health` - API status
- `POST /analyze` - Sentiment analysis

## Run with Docker

Pull and run the API from Docker Hub:

```bash
docker run -d --rm --name sentiment-api -p 8000:8000 yagmurcorum/sentiment-api:latest
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d '{"text":"I love this movie!"}'
```

Build locally and push (maintainers):

```bash
docker build -t sentiment-api:latest -t yagmurcorum/sentiment-api:0.1.0 -t yagmurcorum/sentiment-api:latest .
docker push yagmurcorum/sentiment-api:0.1.0
docker push yagmurcorum/sentiment-api:latest
```

Note: This image contains only the FastAPI backend (port 8000). The UI can be run locally via `streamlit run app.py` (port 8501).

## Live Demo


## Author

Yağmur Çorum - Software Developer

