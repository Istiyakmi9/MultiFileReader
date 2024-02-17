from fastapi import APIRouter, Request, Response, UploadFile, File
from fastapi.responses import JSONResponse
from datetime import date

from service.pdf_file_service import PdfFileService

route = APIRouter()


@route.get("/file_detail")
async def get(request: Request) -> list[dict]:
    pipelines = [{
        "PipelineId": "#123456789",
        "Project": "Mysql Service",
        "Trigger": "restart",
        "Commit": "Message",
        "Stages": 1,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 1
    }, {
        "PipelineId": "#123456789",
        "Project": "EMS Server",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 2,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 2
    }, {
        "PipelineId": "#123456789",
        "Project": "EMS UI",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 3,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 3
    }, {
        "PipelineId": "#123456789",
        "Project": "BottomHalf Site",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 4,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 4
    }, {
        "PipelineId": "#123456789",
        "Project": "New Project",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 1,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 5
    }, {
        "PipelineId": "#123456789",
        "Project": "New Project 2",
        "Trigger": "none",
        "Commit": "Message",
        "Stages": 4,
        "UpdatedOn": date.today(),
        "RunTime": date.today(),
        "ProjectId": 6
    }]

    return pipelines


@route.post("/upload_file")
async def upload_file(file: UploadFile = File(...)) -> Response:
    # Get file details
    filename = file.filename
    content_type = file.content_type
    file_size = file.size
    text_content = "fail"

    try:
        file_content = await file.read()
        fdfFileService = PdfFileService()
        text_content = fdfFileService.read_pdf_file(file_content)
    except Exception as ex:
        print(f"Error: {ex}")

    return JSONResponse(content={
        "content": text_content
    })
