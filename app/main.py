# app/main.py
from fastapi import FastAPI

from app.api.meeting_room import router
from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.app_description)

app.include_router(router)
