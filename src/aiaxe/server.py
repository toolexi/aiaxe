import random
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse,FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static/assets", StaticFiles(directory="ui/dist/static/assets", html=True), name="assets")
app.mount("/ui", StaticFiles(directory="ui/dist"), name="ui")

@app.get("/rand")
async def hello():
    return(str(random.randint(0,100)))

@app.get('/')
async def client():  return FileResponse("ui/dist/index.html")

if __name__ =='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # app.run(debug=True)
