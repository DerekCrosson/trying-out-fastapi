from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"data": "This is the root endpoint"}
