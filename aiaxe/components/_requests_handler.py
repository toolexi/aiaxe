import random
import uvicorn
# from fastapi import APIRouter
from starlette.responses import RedirectResponse,FileResponse
from fastapi import FastAPI
# from components._requests_handler import router
from scripts.build_layout import build_frontend
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def mount_components():
    app.mount("/static/assets", StaticFiles(directory="../ui/dist/static/assets", html=True), name="assets")
    app.mount("/ui", StaticFiles(directory="../ui/dist"), name="ui")

# router = APIRouter()

@app.get("/rand")
async def hello():
    return(str(random.randint(0,100)))

@app.get('/')
async def client():  return FileResponse("../ui/dist/index.html")

def start_components():
    build_frontend()
    mount_components()
    uvicorn.run(app, host="0.0.0.0", port=8000)