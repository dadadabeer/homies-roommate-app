#!/usr/bin/env python3
"""
Test script for the Pure Processor AI Service
Tests the new AI analysis endpoints without file storage
"""

import requests
import base64
import json
from PIL import Image
import io

# AI Service URL
BASE_URL = "http://localhost:8000"

def create_test_image():
    """Create a simple test image and return as base64"""
    # Create a 200x200 test image
    img = Image.new('RGB', (200, 200), color='blue')
    
    # Save to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    
    # Convert to base64
    image_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    return image_base64

def test_health_check():
    """Test the health check endpoint"""
    print("🏥 Testing health check...")
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Health check passed!")
            print(f"   Status: {result['status']}")
            print(f"   Service: {result['service']}")
            print(f"   Capabilities: {result['capabilities']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to AI service. Make sure it's running on port 8000.")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_capabilities():
    """Test the capabilities endpoint"""
    print("\n🔧 Testing capabilities endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/capabilities")
        
        if response.status_code == 200:
            capabilities = response.json()
            print("✅ Capabilities retrieved!")
            for capability, details in capabilities.items():
                print(f"   {capability}: {details['description']}")
            return capabilities
        else:
            print(f"❌ Failed to get capabilities: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_image_analysis():
    """Test the image analysis endpoint"""
    print("\n🖼️ Testing image analysis...")
    
    # Create test image
    image_base64 = create_test_image()
    
    # Prepare request
    request_data = {
        "user_id": "test_user_123",
        "image_data": image_base64,
        "image_type": "profile",
        "image_metadata": {
            "original_filename": "test_profile.jpg",
            "upload_time": "2024-01-15T10:30:00Z"
        }
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/analyze-image",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Image analysis successful!")
            print(f"   User ID: {result['user_id']}")
            print(f"   Analysis Type: {result['analysis_type']}")
            print(f"   Confidence Score: {result['confidence_score']}")
            print(f"   Processing Time: {result['processing_time_ms']}ms")
            print(f"   Cleanliness Score: {result['results']['cleanliness_score']}")
            print(f"   Room Style: {result['results']['room_style']}")
            return result
        else:
            print(f"❌ Image analysis failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_text_analysis():
    """Test the text analysis endpoint"""
    print("\n📝 Testing text analysis...")
    
    # Sample user description
    sample_text = """
    I'm a software developer who loves hiking and cooking. 
    I'm very organized and prefer a clean, quiet environment. 
    I usually wake up early and go to bed by 11 PM. 
    I'm looking for a roommate who is also clean and respectful of quiet hours.
    """
    
    request_data = {
        "user_id": "test_user_123",
        "text": sample_text,
        "text_type": "profile_description"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/analyze-text",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Text analysis successful!")
            print(f"   User ID: {result['user_id']}")
            print(f"   Analysis Type: {result['analysis_type']}")
            print(f"   Sentiment: {result['results']['sentiment']}")
            print(f"   Personality Traits: {result['results']['personality_traits']}")
            print(f"   Lifestyle Preferences: {result['results']['lifestyle_preferences']}")
            print(f"   Communication Style: {result['results']['communication_style']}")
            return result
        else:
            print(f"❌ Text analysis failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_user_matching():
    """Test the user matching endpoint"""
    print("\n🤝 Testing user matching...")
    
    # Create test user profiles
    user1_profile = {
        "user_id": "user_1",
        "name": "John Doe",
        "interests": ["hiking", "cooking", "reading"],
        "lifestyle": "organized and quiet",
        "description": "Software developer who loves outdoor activities",
        "preferences": {
            "cleanliness": "high",
            "noise_level": "low",
            "schedule": "early_bird"
        }
    }
    
    user2_profile = {
        "user_id": "user_2", 
        "name": "Jane Smith",
        "interests": ["yoga", "meditation", "cooking"],
        "lifestyle": "peaceful and clean",
        "description": "Graduate student who values quiet study time",
        "preferences": {
            "cleanliness": "high",
            "noise_level": "low", 
            "schedule": "early_bird"
        }
    }
    
    request_data = {
        "user1_profile": user1_profile,
        "user2_profile": user2_profile,
        "user1_images": [create_test_image()],  # Add test images
        "user2_images": [create_test_image()]
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/match-users",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ User matching successful!")
            print(f"   Match Score: {result['match_score']}")
            print(f"   Compatibility Factors: {result['compatibility_factors']}")
            print(f"   Text Compatibility: {result['text_compatibility']}")
            print(f"   Image Compatibility: {result['image_compatibility']}")
            print(f"   Lifestyle Compatibility: {result['lifestyle_compatibility']}")
            return result
        else:
            print(f"❌ User matching failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def test_profile_analysis():
    """Test the comprehensive profile analysis endpoint"""
    print("\n👤 Testing profile analysis...")
    
    # Test data
    user_id = "test_user_456"
    text_data = "I'm a clean, organized person who values quiet time and early mornings."
    image_data = create_test_image()
    
    request_data = {
        "user_id": user_id,
        "text_data": text_data,
        "image_data": image_data
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/analyze-profile",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Profile analysis successful!")
            print(f"   User ID: {result['user_id']}")
            print(f"   Text Analysis: {'✅' if result['text_analysis'] else '❌'}")
            print(f"   Image Analysis: {'✅' if result['image_analysis'] else '❌'}")
            print(f"   Overall Personality: {result['overall_personality']}")
            return result
        else:
            print(f"❌ Profile analysis failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def main():
    """Run all tests"""
    print("🚀 Starting Pure Processor AI Service Tests")
    print("=" * 60)
    
    # Test health check first
    if not test_health_check():
        print("\n❌ AI Service is not running. Please start it first:")
        print("   cd ai_service")
        print("   pip install -r requirements.txt")
        print("   uvicorn app:app --reload --host 0.0.0.0 --port 8000")
        return
    
    # Test capabilities
    capabilities = test_capabilities()
    
    # Test individual analysis endpoints
    image_result = test_image_analysis()
    text_result = test_text_analysis()
    match_result = test_user_matching()
    profile_result = test_profile_analysis()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    tests = [
        ("Health Check", True),
        ("Capabilities", capabilities is not None),
        ("Image Analysis", image_result is not None),
        ("Text Analysis", text_result is not None),
        ("User Matching", match_result is not None),
        ("Profile Analysis", profile_result is not None)
    ]
    
    passed = 0
    for test_name, success in tests:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if success:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("\n🎉 All tests passed! Your Pure Processor AI Service is working correctly.")
        print("\n📋 Next steps:")
        print("   1. Integrate with your Spring Boot backend")
        print("   2. Implement real AI models (replace mock data)")
        print("   3. Add more sophisticated matching algorithms")
        print("   4. Set up monitoring and logging")
    else:
        print(f"\n⚠️  {len(tests) - passed} test(s) failed. Check the AI service logs.")

if __name__ == "__main__":
    main() 