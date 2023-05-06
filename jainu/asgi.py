import os

from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from api.endpoints import api_router

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jainu.settings")
apps.populate(settings.INSTALLED_APPS)


def get_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="")
    app.mount("/django", WSGIMiddleware(get_wsgi_application()))
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app


app = get_application()