from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from repositories.database import Base, engine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the MVP API!"}
