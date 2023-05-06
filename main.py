from fastapi import FastAPI
from jainu import asgi

app = asgi.get_application()
