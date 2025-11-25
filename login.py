from fastapi import FastAPI
from fastapi import Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VALID_PASSWORD = "PyLEaRn@671/1/2026_USER"

@app.post("/login")
def login(data: dict = Body(...)):
    if data["password"] == VALID_PASSWORD:
        return {"success": True}
    return {"success": False}
