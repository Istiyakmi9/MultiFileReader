import uvicorn
from fastapi import FastAPI
from controller.pdf_file_controller import route

app = FastAPI()

app.include_router(route)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
