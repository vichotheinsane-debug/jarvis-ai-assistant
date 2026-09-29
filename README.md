# jarvis-ai-assistant

A modular, secure personal AI assistant designed to run as a local control center with voice, automation, AI orchestration, memory, plugins, and a futuristic control dashboard.

## Features

- Natural-language command interpretation
- AI provider abstraction (OpenAI, Anthropic, Google, local fallback)
- Voice STT/TTS abstraction
- Safe PC automation with an allowlist and confirmation gates
- Memory persistence with SQLite
- Plugin registry for weather, Spotify, Discord, PC, reminders, and IoT-ready modules
- REST API with API-key protection
- Futuristic status dashboard
- Night mode / suspend workflow with OS-aware suspension logic

## Stack

- Python 3.11+
- FastAPI
- SQLite
- Pydantic + python-dotenv
- pytest
- psutil

## Quick start

```bash
git clone https://github.com/vichotheinsane-debug/jarvis-ai-assistant.git
cd jarvis-ai-assistant
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Then open http://localhost:8000

## Environment

Copy `.env.example` and populate the optional values you want to enable. The app will only enable features that are configured.

## Security

- Dangerous actions require confirmation.
- OS actions are limited to a safe allowlist.
- Secrets are never logged.
- `/api/*` endpoints require an API key.

## Tests

```bash
pytest -q
```
