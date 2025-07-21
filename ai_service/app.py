from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import base64
import io
from PIL import Image
import numpy as np

app = FastAPI(
    title="Homies AI Service",
    description="Pure AI processor for NLP and image analysis in the Homies roommate matching app",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],  # Frontend and Backend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models for Pure Processing
class UserProfile(BaseModel):
    user_id: str
    name: str
    interests: List[str]
    lifestyle: str
    description: str
    preferences: Dict[str, Any]

class ImageAnalysisRequest(BaseModel):
    user_id: str
    image_data: str  # Base64 encoded image
    image_type: str  # profile, room, lifestyle, etc.
    image_metadata: Optional[Dict[str, Any]] = None

class TextAnalysisRequest(BaseModel):
    user_id: str
    text: str
    text_type: str  # description, bio, preferences, etc.

class MatchRequest(BaseModel):
    user1_profile: UserProfile
    user2_profile: UserProfile
    user1_images: Optional[List[str]] = None  # List of base64 encoded images
    user2_images: Optional[List[str]] = None  # List of base64 encoded images

class AnalysisResponse(BaseModel):
    user_id: str
    analysis_type: str
    results: Dict[str, Any]
    confidence_score: float
    processing_time_ms: float

class MatchResponse(BaseModel):
    match_score: float
    compatibility_factors: List[str]
    image_compatibility: Optional[float] = None
    text_compatibility: Optional[float] = None
    lifestyle_compatibility: Optional[float] = None
    detailed_analysis: Dict[str, Any]

# Health and Status Endpoints
@app.get("/")
def read_root():
    return {
        "message": "Homies AI Service - Pure Processor", 
        "status": "healthy",
        "service_type": "ai_processor"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "service": "ai_processor",
        "capabilities": ["image_analysis", "text_analysis", "user_matching"]
    }

@app.get("/capabilities")
def get_capabilities():
    """Return available AI processing capabilities"""
    return {
        "image_analysis": {
            "description": "Analyze images for lifestyle, cleanliness, and personality indicators",
            "input_format": "base64_encoded_image",
            "output": ["cleanliness_score", "lifestyle_indicators", "room_style", "objects_detected"]
        },
        "text_analysis": {
            "description": "Analyze text for sentiment, personality traits, and preferences",
            "input_format": "plain_text",
            "output": ["sentiment", "personality_traits", "lifestyle_preferences", "communication_style"]
        },
        "user_matching": {
            "description": "Calculate compatibility scores between two users",
            "input_format": "user_profiles_and_images",
            "output": ["match_score", "compatibility_factors", "detailed_analysis"]
        }
    }

# Pure AI Processing Endpoints
@app.post("/analyze-image")
async def analyze_image(request: ImageAnalysisRequest):
    """
    Pure image analysis - receives image data and returns analysis results
    
    Args:
        request: ImageAnalysisRequest with base64 image data
    
    Returns:
        AnalysisResponse with image analysis results
    """
    import time
    start_time = time.time()
    
    try:
        # Decode base64 image
        image_data = base64.b64decode(request.image_data)
        image = Image.open(io.BytesIO(image_data))
        
        # TODO: Implement actual computer vision analysis
        # This is where you'd use libraries like:
        # - OpenCV for object detection
        # - TensorFlow/PyTorch for image classification
        # - Face recognition libraries for profile photos
        
        # Mock analysis results (replace with real AI processing)
        analysis_results = {
            "image_type": request.image_type,
            "image_size": image.size,
            "image_format": image.format,
            "color_palette": ["#FF0000", "#00FF00", "#0000FF"],  # Mock data
            "objects_detected": ["furniture", "electronics", "books"],  # Mock data
            "cleanliness_score": 0.85,  # Mock score (0-1)
            "lifestyle_indicators": ["organized", "tech-savvy", "studious"],  # Mock data
            "room_style": "modern_minimalist",  # Mock classification
            "clutter_level": "low",  # low, medium, high
            "aesthetic_preference": "minimalist",  # minimalist, cozy, modern, etc.
            "personality_hints": ["detail-oriented", "practical", "ambitious"]
        }
        
        processing_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        response = AnalysisResponse(
            user_id=request.user_id,
            analysis_type="image_analysis",
            results=analysis_results,
            confidence_score=0.92,
            processing_time_ms=round(processing_time, 2)
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image analysis failed: {str(e)}")

@app.post("/analyze-text")
async def analyze_text(request: TextAnalysisRequest):
    """
    Pure text analysis - receives text data and returns analysis results
    
    Args:
        request: TextAnalysisRequest with text to analyze
    
    Returns:
        AnalysisResponse with text analysis results
    """
    import time
    start_time = time.time()
    
    try:
        # TODO: Implement actual NLP analysis
        # This is where you'd use libraries like:
        # - spaCy for text processing
        # - Transformers for sentiment analysis
        # - NLTK for keyword extraction
        
        # Mock analysis results (replace with real NLP processing)
        analysis_results = {
            "text_type": request.text_type,
            "text_length": len(request.text),
            "sentiment": "positive",  # positive, negative, neutral
            "sentiment_score": 0.78,  # -1 to 1
            "keywords": ["friendly", "clean", "quiet", "organized", "ambitious"],
            "personality_traits": ["extroverted", "organized", "ambitious", "friendly"],
            "lifestyle_preferences": ["early_bird", "clean_freak", "social", "studious"],
            "communication_style": "direct_and_friendly",  # direct, friendly, formal, casual
            "stress_level": "low",  # low, medium, high
            "social_preference": "moderate",  # introverted, moderate, extroverted
            "cleanliness_priority": "high",  # low, medium, high
            "noise_tolerance": "low",  # low, medium, high
            "schedule_preference": "structured"  # flexible, structured, strict
        }
        
        processing_time = (time.time() - start_time) * 1000
        
        response = AnalysisResponse(
            user_id=request.user_id,
            analysis_type="text_analysis",
            results=analysis_results,
            confidence_score=0.88,
            processing_time_ms=round(processing_time, 2)
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text analysis failed: {str(e)}")

@app.post("/match-users")
async def match_users(request: MatchRequest):
    """
    Pure user matching - receives user data and returns compatibility scores
    
    Args:
        request: MatchRequest with user profiles and optional images
    
    Returns:
        MatchResponse with compatibility analysis
    """
    import time
    start_time = time.time()
    
    try:
        # TODO: Implement actual AI matching logic
        # This would combine:
        # - Text analysis results
        # - Image analysis results  
        # - Preference matching algorithms
        # - Machine learning models for compatibility prediction
        
        # Mock matching algorithm (replace with real AI)
        text_compatibility = 0.85
        image_compatibility = 0.78 if request.user1_images and request.user2_images else None
        lifestyle_compatibility = 0.92
        
        # Calculate overall match score
        if image_compatibility:
            match_score = (text_compatibility + image_compatibility + lifestyle_compatibility) / 3
        else:
            match_score = (text_compatibility + lifestyle_compatibility) / 2
        
        compatibility_factors = [
            "Similar lifestyle preferences",
            "Compatible communication styles", 
            "Matching cleanliness standards",
            "Shared interests in technology and organization"
        ]
        
        if image_compatibility:
            compatibility_factors.append("Compatible room aesthetics")
        
        detailed_analysis = {
            "text_analysis": {
                "communication_compatibility": 0.88,
                "personality_alignment": 0.82,
                "lifestyle_similarity": 0.90
            },
            "image_analysis": {
                "aesthetic_compatibility": 0.75 if image_compatibility else None,
                "cleanliness_alignment": 0.85,
                "space_organization_similarity": 0.80
            },
            "preference_matching": {
                "schedule_compatibility": 0.92,
                "social_preference_alignment": 0.78,
                "noise_tolerance_match": 0.85
            }
        }
        
        processing_time = (time.time() - start_time) * 1000
        
        response = MatchResponse(
            match_score=round(match_score, 2),
            compatibility_factors=compatibility_factors,
            image_compatibility=image_compatibility,
            text_compatibility=text_compatibility,
            lifestyle_compatibility=lifestyle_compatibility,
            detailed_analysis=detailed_analysis
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Matching failed: {str(e)}")

@app.post("/batch-analyze")
async def batch_analyze(requests: List[ImageAnalysisRequest]):
    """
    Batch image analysis for efficiency
    
    Args:
        requests: List of ImageAnalysisRequest objects
    
    Returns:
        List of AnalysisResponse objects
    """
    try:
        results = []
        
        for request in requests:
            # Process each image (could be parallelized for better performance)
            result = await analyze_image(request)
            results.append(result)
        
        return {
            "analyses": results,
            "total_processed": len(results),
            "batch_size": len(requests)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch analysis failed: {str(e)}")

@app.post("/analyze-profile")
async def analyze_profile(
    user_id: str,
    text_data: Optional[str] = None,
    image_data: Optional[str] = None
):
    """
    Comprehensive profile analysis combining text and image data
    
    Args:
        user_id: ID of the user
        text_data: Optional text description/bio
        image_data: Optional base64 encoded profile image
    
    Returns:
        Comprehensive profile analysis
    """
    try:
        profile_analysis = {
            "user_id": user_id,
            "text_analysis": None,
            "image_analysis": None,
            "overall_personality": {},
            "lifestyle_summary": {},
            "compatibility_indicators": []
        }
        
        # Analyze text if provided
        if text_data:
            text_request = TextAnalysisRequest(
                user_id=user_id,
                text=text_data,
                text_type="profile"
            )
            text_result = await analyze_text(text_request)
            profile_analysis["text_analysis"] = text_result.results
        
        # Analyze image if provided
        if image_data:
            image_request = ImageAnalysisRequest(
                user_id=user_id,
                image_data=image_data,
                image_type="profile"
            )
            image_result = await analyze_image(image_request)
            profile_analysis["image_analysis"] = image_result.results
        
        # Combine analyses for overall profile
        if profile_analysis["text_analysis"] and profile_analysis["image_analysis"]:
            profile_analysis["overall_personality"] = {
                "primary_traits": ["organized", "ambitious", "friendly"],
                "communication_style": "direct_and_friendly",
                "social_preference": "moderate",
                "lifestyle_type": "structured_and_clean"
            }
        elif profile_analysis["text_analysis"]:
            profile_analysis["overall_personality"] = profile_analysis["text_analysis"]
        elif profile_analysis["image_analysis"]:
            profile_analysis["overall_personality"] = profile_analysis["image_analysis"]
        
        return profile_analysis
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Profile analysis failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 