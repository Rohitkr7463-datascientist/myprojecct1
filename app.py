# /// script 
# requires-python = ">=3.13"
# dependencies = [
#    "fastapi",
#    "uvicorn",
#    "requests",
# ]
# ///

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ Import fixed

app = FastAPI()

# ✅ Fixed middleware syntax and imported CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # ✅ Uppercase method names
    allow_headers=["*"],
)

@app.get("/")  # ✅ Added missing decorator
def home():
    return {"message": "My name is Rohit and I am trying to do the TDS project 1."}  # ✅ Fixed response format

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
