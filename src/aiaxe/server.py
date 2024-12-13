import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/rand")
async def hello():
    return(str(random.randint(0,100)))

if __name__ =='__main__':
    app.run(debug=True)
