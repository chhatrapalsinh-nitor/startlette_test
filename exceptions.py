from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse


HTML_404_PAGE = "404 Page not gound"
HTML_500_PAGE = "500 Internal server error"


async def not_found(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)

async def server_error(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_500_PAGE, status_code=exc.status_code)

class InvalidMobileError(Exception):
    """Raise an error if grater or less than 10 digits in mobile."""

    def __init__(self, value:int, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)