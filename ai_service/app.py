from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Homies AI Service",
    description="AI microservice for NLP and image matching in the Homies roommate matching app",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserProfile(BaseModel):
    name: str
    interests: List[str]
    lifestyle: str
    description: str

class MatchRequest(BaseModel):
    user_profile: UserProfile
    preferences: List[str]

@app.get("/")
def read_root():
    return {"message": "Homies AI Service is running", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ai"}

@app.post("/match")
def match_users(request: MatchRequest):
    """
    AI-powered user matching endpoint
    """
    try:
        # TODO: Implement actual AI matching logic
        # For now, return a mock response
        return {
            "matches": [
                {
                    "user_id": "user_1",
                    "score": 0.85,
                    "compatibility_reasons": ["Similar interests", "Compatible lifestyle"]
                },
                {
                    "user_id": "user_2", 
                    "score": 0.72,
                    "compatibility_reasons": ["Shared hobbies"]
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-text")
def analyze_text(text: str):
    """
    NLP analysis endpoint for user descriptions
    """
    try:
        # TODO: Implement actual NLP analysis
        return {
            "sentiment": "positive",
            "keywords": ["friendly", "clean", "quiet"],
            "personality_traits": ["extroverted", "organized"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 