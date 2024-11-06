from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse, Response
from starlette.exceptions import HTTPException as StarletteHTTPException

async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 401:
        return RedirectResponse(url="/")
    if exc.status_code == 404:
        return RedirectResponse(url="/")
    return Response(content="Error managed via HTTP module", status_code=400)

async def starlette_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return RedirectResponse(url="/")
    return Response(content="Error managed via HTTP module", status_code=exc.status_code)
