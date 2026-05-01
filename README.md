# Assistant IA API

A personal learning project built step by step to explore how to design, version, and improve an AI-powered API with FastAPI.

The project starts as a simple FastAPI application, then evolves into an AI Assistant API, and finally into an AI Conversational Agent.

## Current Version

**v0.1.0**

## Project Goal

The main goal of this project is to progressively build an AI-based backend system while following a clean development process with:
- FastAPI
- Git and GitHub versioning
- incremental releases
- clear project documentation

## Current Features

At this stage, the project includes:
- a FastAPI application
- a root endpoint `/`
- a health check endpoint `/health`
- a basic project structure ready for future evolution

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Git
- GitHub

## Project Structure

```text
assistant-ia-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/TokySandratra/AI-Chatbot.git
```

Create and activate a virtual environment:

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Start the FastAPI development server with:

```bash
uvicorn app.main:app --reload
```

Then open:

- API root: `http://127.0.0.1:8000/`
- Health check: `http://127.0.0.1:8000/health`
- Swagger UI: `http://127.0.0.1:8000/docs`

## API Endpoints

### `GET /`
Returns a basic welcome message.

### `GET /health`
Returns the API health status.

## Roadmap

This project is intentionally built in phases.

- **v0.1.0** — FastAPI base project
- **v0.2.0** — First AI endpoint
- **v0.3.0** — AI assistant with document support
- **v1.0.0** — AI conversational agent

## Versioning Strategy

The project uses Git tags to mark stable milestones.

Example:
- `v0.1.0` → initial FastAPI project setup
- `v0.2.0` → first AI integration
- `v0.3.0` → document-based assistant
- `v1.0.0` → conversational agent release

## Git Workflow

A simple Git workflow is used for project evolution:

- `main` for stable versions
- `dev` for ongoing development
- `feature/...` branches for specific tasks

Example feature branches:
- `feature/init-fastapi`
- `feature/ai-endpoint`
- `feature/document-support`
- `feature/conversation-memory`

## Author
Toky RASAMOELINA 
Personal project for learning, experimentation, and portfolio development.