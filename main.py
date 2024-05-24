import uvicorn
from fastapi import FastAPI
from controller.pdf_file_controller import route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
