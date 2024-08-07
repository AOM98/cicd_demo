# /app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# Counter state stored in-memory
class Counter:
    value = 0


counter = Counter()

# FastAPI instance
app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3003",  # Allow your Angular app to access the API
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Pydantic model for responses
class CounterResponse(BaseModel):
    value: int


@app.get("/counter", response_model=CounterResponse)
async def get_counter():
    """Return the current value of the counter."""
    return CounterResponse(value=counter.value)


@app.post("/counter/increment", response_model=CounterResponse)
async def increment_counter():
    """Increment the counter by 1."""
    counter.value += 1
    return CounterResponse(value=counter.value)


@app.post("/counter/decrement", response_model=CounterResponse)
async def decrement_counter():
    """Decrement the counter by 1."""
    counter.value -= 1
    return CounterResponse(value=counter.value)


@app.post("/counter/reset", response_model=CounterResponse)
async def reset_counter():
    """Reset the counter to 0."""
    counter.value = 0
    return CounterResponse(value=counter.value)
