from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline
import re

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

# Sentiment analysis modelini yükle
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    return_all_scores=True
)

class TextRequest(BaseModel):
    text: str = Field(..., min_length=3, max_length=500, description="English sentence to analyze")

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/analyze")
def analyze_sentiment(request: TextRequest):
    # Boşluklardan oluşan veya boş metin kontrolü
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    # Anlamsız metin kontrolü (sadece noktalama, tek harf vs.)
    cleaned = re.sub(r'[^A-Za-z0-9]', '', request.text)
    if not cleaned or len(cleaned) < 2:
        raise HTTPException(
            status_code=400,
            detail="Please enter a meaningful sentence, not just a single character or punctuation."
        )

    # Model ile analiz
    results = sentiment_analyzer(request.text)
    best_sentiment = max(results[0], key=lambda x: x['score'])

    return {
        "text": request.text,
        "sentiment": best_sentiment['label'],
        "confidence": round(best_sentiment['score'], 3),
        "all_scores": results[0]
    }