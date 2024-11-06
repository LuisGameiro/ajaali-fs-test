from fastapi import Response, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from ajaali.routes.view.search_flights import search_flights_route
from ajaali.exception import http_exception_handler, starlette_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(
    exception_handlers={
        HTTPException: http_exception_handler,
        StarletteHTTPException: starlette_exception_handler,
    }
)

app.mount("/static", StaticFiles(directory="ajaali/static"), name="static")

app.include_router(search_flights_route, tags=["Pages"])

# Suppress favicon requests by returning 204 No Content
@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)
