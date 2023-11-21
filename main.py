from distutils.log import debug
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.templating import Jinja2Templates
import json
from models import User
from typing import List
from database import get_all_users, create_student
from exceptions import not_found, server_error
import uvicorn
import sys


templates = Jinja2Templates(directory="templates")


async def index(request:Request):
    create_student()
    return PlainTextResponse(content="Hello {name} !!!")


async def json_responce(request:Request):
    context = {
        "message" : "Hello world"
    }
    with open("load.json") as file:
        data = json.load(file)
        users : List[User] = [User(**item) for item in data]
        print(users[0])
        # print(users[0].model_dump())
    return JSONResponse(content=data)

async def html_endpoint(request:Request):
    users=get_all_users()
    context={"request":request,"users":users}
    return templates.TemplateResponse("index.html", context)

routes = [
    Route("/", endpoint=index),
    Route("/json", endpoint=json_responce),
    Route("/html", endpoint=html_endpoint),
]

exception_handlers = {
    404: not_found,
    500: server_error
}

app = Starlette(
    debug=True,
    routes=routes,
    exception_handlers=exception_handlers
)



# if __name__ == '__main__':
#     uvicorn.run("main:app", host='0.0.0.0', port=5000)


