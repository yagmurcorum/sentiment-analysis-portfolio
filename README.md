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

## Live Demo

[Coming Soon - Heroku Deployment]

## Author

Yağmur Çorum - Software Developer

