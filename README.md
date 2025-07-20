# Homies - Roommate Matching App

A full-stack web application for AI-powered roommate matching, built with modern technologies.

## 🏗️ Architecture

The project consists of three main components:

- **Backend**: Kotlin + Spring Boot REST API
- **AI Service**: Python FastAPI microservice for NLP and image matching
- **Frontend**: Next.js (React) web application with Tailwind CSS

## 📁 Project Structure

```
homies_two/
├── backend/                 # Spring Boot + Kotlin backend
│   ├── src/
│   │   ├── main/
│   │   │   ├── kotlin/com/homies/backend/
│   │   │   │   └── BackendApplication.kt
│   │   │   └── resources/
│   │   │       └── application.properties
│   │   └── test/
│   ├── build.gradle.kts
│   └── settings.gradle.kts
├── ai_service/             # FastAPI AI microservice
│   ├── app.py
│   └── requirements.txt
├── frontend/               # Next.js frontend
│   ├── src/
│   │   └── app/
│   │       ├── globals.css
│   │       ├── layout.tsx
│   │       └── page.tsx
│   ├── package.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── tsconfig.json
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- **Java 17+** (for Spring Boot backend)
- **Python 3.8+** (for AI service)
- **Node.js 18+** (for Next.js frontend)
- **PostgreSQL** (for database)

### Backend (Spring Boot)

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Run the application:**
   ```bash
   ./gradlew bootRun
   ```
   
   The backend will start on `http://localhost:8080`

3. **Build the project:**
   ```bash
   ./gradlew build
   ```

### AI Service (FastAPI)

1. **Navigate to AI service directory:**
   ```bash
   cd ai_service
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the service:**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```
   
   The AI service will start on `http://localhost:8000`

4. **Access API documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Frontend (Next.js)

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```
   
   The frontend will start on `http://localhost:3000`

4. **Build for production:**
   ```bash
   npm run build
   npm start
   ```

## 🔧 Configuration

### Backend Configuration

Edit `backend/src/main/resources/application.properties` to configure:
- Database connection (PostgreSQL)
- Server port
- Security settings

### AI Service Configuration

The AI service is configured in `ai_service/app.py`:
- CORS settings for frontend communication
- API endpoints for matching and analysis

### Frontend Configuration

- Tailwind CSS configuration: `frontend/tailwind.config.js`
- Next.js configuration: `frontend/next.config.js`
- TypeScript configuration: `frontend/tsconfig.json`

## 🛠️ Development

### Backend Development
- Main application: `BackendApplication.kt`
- Add controllers, services, and repositories in the `com.homies.backend` package
- Database entities should be in a `model` or `entity` package

### AI Service Development
- Main application: `app.py`
- Add new endpoints for additional AI features
- Implement actual NLP and image matching logic

### Frontend Development
- Main page: `src/app/page.tsx`
- Layout: `src/app/layout.tsx`
- Add components in `src/components/`
- Styling with Tailwind CSS

## 🔌 API Endpoints

### Backend (Port 8080)
- `GET /` - Health check
- `POST /api/users` - Create user
- `GET /api/users` - Get users
- `POST /api/matches` - Create match

### AI Service (Port 8000)
- `GET /` - Health check
- `POST /match` - AI-powered user matching
- `POST /analyze-text` - NLP text analysis
- `GET /docs` - API documentation

## 🧪 Testing

### Backend Testing
```bash
cd backend
./gradlew test
```

### AI Service Testing
```bash
cd ai_service
python -m pytest
```

### Frontend Testing
```bash
cd frontend
npm test
```

## 📦 Deployment

Each service can be deployed independently:

- **Backend**: Deploy as a JAR file with `./gradlew build`
- **AI Service**: Deploy with Docker or directly with uvicorn
- **Frontend**: Deploy to Vercel, Netlify, or any static hosting service

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. 