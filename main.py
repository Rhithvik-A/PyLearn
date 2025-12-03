from fastapi import FastAPI, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Login Logic
VALID_PASSWORD = "PyLEaRn@671/1/2026_USER"

@app.post("/login")
def login(data: dict = Body(...)):
    if data["password"] == VALID_PASSWORD:
        return {"success": True}
    return {"success": False}

# Code Conversion Logic
client = genai.Client(api_key="AIzaSyB8QTPh4nMAo5VZjjBzlyn0Bp30YTsIjRo")

@app.get("/convert_code")
def convert_code(Question: str = Query(..., description="Your question")):
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=Question
            )
            return {"answer": response.text}
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)
    return {"error": "Failed to get response after retries."}
