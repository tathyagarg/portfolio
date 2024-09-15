from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import countdown

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(countdown.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=5000)
