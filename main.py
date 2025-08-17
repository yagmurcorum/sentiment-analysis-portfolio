from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline
import re

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

# Use lazy loading so that large model initialization does not block requests.
sentiment_analyzer = None

def get_sentiment_analyzer():
    global sentiment_analyzer
    if sentiment_analyzer is None:
        sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest",
            return_all_scores=True
        )
    return sentiment_analyzer

class TextRequest(BaseModel):
    text: str = Field(..., min_length=3, max_length=500, description="English sentence to analyze")

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API is running!"}

@app.get("/health")
def health_check():
    # Health endpoint independent from the model; always responds quickly
    return {"status": "ok"}

@app.post("/analyze")
def analyze_sentiment(request: TextRequest):
    # Reject empty or whitespace-only text
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    # Reject meaningless text (only punctuation, single character, etc.)
    cleaned = re.sub(r'[^A-Za-z0-9]', '', request.text)
    if not cleaned or len(cleaned) < 2:
        raise HTTPException(
            status_code=400,
            detail="Please enter a meaningful sentence, not just a single character or punctuation."
        )

    # Lazily load the model when needed and run inference
    analyzer = get_sentiment_analyzer()
    results = analyzer(request.text)
    best_sentiment = max(results[0], key=lambda x: x['score'])

    return {
        "text": request.text,
        "sentiment": best_sentiment['label'],
        "confidence": round(best_sentiment['score'], 3),
        "all_scores": results[0]
    }