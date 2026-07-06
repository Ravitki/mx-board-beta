from fastapi import FastAPI

app = FastAPI()

@app.get("/version")
async def get_version():
    return {"version": "1.0.0"}
