from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from model.query_request import QueryRequest

import google.generativeai as genai
import os

route = APIRouter()


@route.post("/api/generate/response")
async def user_query(query_request: QueryRequest) -> Response:
    print(query_request.query)

    genai.configure(api_key="AIzaSyBpzjEBd9w3GcQgbfAHMFexQ1VNP5ixho8")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query_request.query)
    return JSONResponse(content={
        "content": response.text
    })
