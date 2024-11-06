from typing import List
from fastapi import Path, Form, Request, Query, HTTPException
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from ajaali.services.flight_service import get_flights_filter_and_sort
from ajaali.utils.build_url import build_new_url
from ajaali.template import templates
from datetime import datetime
from ajaali.models.user import user_example
from ajaali.models.search import SortOption, default_sort, Filters, Search

search_flights_route = APIRouter()

@search_flights_route.get("/", response_class=HTMLResponse)
async def get_search(request: Request):
    """
    Render the search-flights.html template.

    Args:
        request (Request): The request object.

    Returns:
        TemplateResponse: The rendered HTML response.
    """

    response = templates.TemplateResponse(
        "pages/search-flights.html",
        {
            "request": request,
            "status_code": 200,
            "user": user_example,
            "flights": {},
            "search": Search(),
            "filters": Filters(),
            "sort": SortOption.TOP_FLIGHTS.value,
        },
    )
    return response

@search_flights_route.get(
    "/search/{departure}/{destination}/{departure_date}/{return_date}",
    response_class=HTMLResponse,
)
async def get_search_flights(
    request: Request,
    departure: str = Path(..., description="Departure location"),
    destination: str = Path(..., description="Destination location"),
    departure_date: str = Path(..., description="Departure date in YYYY-MM-DD format"),
    return_date: str = Path(..., description="Return date in YYYY-MM-DD format"),
    sort: Optional[str] = Query(None),
    stops: Optional[str] = Query(None),
    airlines: Optional[str] = Query(None),
):
    """
    Render the search-flights.html template based on the provided search parameters.

    Args:
        request (Request): The request object.
        departure (str): Departure location.
        destination (str): Destination location.
        departure_date (str): Date of departure in YYYY-MM-DD format.
        return_date (str): Date of return in YYYY-MM-DD format.
        sort (Optional[str]): Sort option.
        stops (Optional[str]): Number of stops.
        airlines (Optional[str]): List of airlines.

    Returns:
        TemplateResponse: The rendered HTML response.
    """
    
    if not departure:
        raise HTTPException(status_code=422, detail="Departure location is required.")
    if not destination:
        raise HTTPException(status_code=422, detail="Destination location is required.")
    
    try:
        departure_date = datetime.strptime(departure_date, "%Y-%m-%d")
        return_date = datetime.strptime(return_date, "%Y-%m-%d")

    except ValueError:
        raise HTTPException(
            status_code=422, detail="Invalid return date format. Expected YYYY-MM-DD."
        )

    search = Search(
        departure=departure,
        destination=destination,
        departure_date=departure_date,
        return_date=return_date,
    )
    airlines_list = airlines.split(",") if airlines else []

    filters = Filters(stops=stops, airlines=airlines_list)
    sort_option = SortOption(value=sort or default_sort.value)
    flights_data = get_flights_filter_and_sort(search, filters, sort_option)

    response = templates.TemplateResponse(
        "pages/search-flights.html",
        {
            "request": request,
            "status_code": 200,
            "user": user_example,
            "flights": flights_data[:20],
            "len_flights": len(flights_data),
            "search": search,
            "filters": filters,
            "sort": sort_option.value,
        },
    )

    return response

@search_flights_route.post("/search", response_class=HTMLResponse)
async def search(
    request: Request,
    departure: str = Form(...),
    destination: str = Form(...),
    departure_date: str = Form(...),
    return_date: str = Form(...),
    stops: Optional[int | str] = Form(None),
    airlines: Optional[List[str]] = Form([]),
    sort: Optional[str] = Form(default_sort.value),
):
    """
    Handle the search post request and render the flights-result.html template.

    Args:
        request (Request): The request object.
        departure (str): Departure location.
        destination (str): Destination location.
        departure_date (str): Date of departure.
        return_date (str): Date of return.
        stops (Optional[int | str]): Number of stops.
        airlines (Optional[List[str]]): List of airlines.
        sort (Optional[str]): Sort option.

    Returns:
        TemplateResponse: The rendered partial HTML response.
    """
    if not departure:
        raise HTTPException(status_code=422, detail="Departure location is required.")
    if not destination:
        raise HTTPException(status_code=422, detail="Destination location is required.")
    
    search = Search(
        departure=departure,
        destination=destination,
        departure_date=departure_date,
        return_date=return_date,
    )

    stops = None if stops == "None" else stops


    filters = Filters(stops=stops, airlines=airlines)
    sort_option = SortOption(value=sort or default_sort.value)
    flights_data = get_flights_filter_and_sort(search, filters, sort_option)
    new_url = build_new_url(request, search, filters, sort)

    response = templates.TemplateResponse(
        "partials/search-flights/flights-result.html",
        {
            "request": request,
            "status_code": 200,
            "flights": flights_data[:20],
            "len_flights": len(flights_data),
            "search": search,
            "filters": filters,
            "sort": sort_option.value,
            "new_url": new_url,
        },
    )
    return response

@search_flights_route.post("/more-flights", response_class=HTMLResponse)
async def more_flights(
    request: Request,
    departure: str = Form(...),
    destination: str = Form(...),
    departure_date: str = Form(...),
    return_date: str = Form(...),
    stops: Optional[int | str] = Form(None),
    airlines: Optional[List[str]] = Form([]),
    sort: Optional[str] = Form(default_sort.value),
):
    """
    Handle the POST request to fetch more flight results.

    Args:
        request (Request): The request object.
        departure (str): The departure location.
        destination (str): The destination location.
        departure_date (str): The departure date.
        return_date (str): The return date.
        stops (Optional[int | str]): The number of stops (optional).
        airlines (Optional[List[str]]): List of preferred airlines (optional).
        sort (Optional[str]): The sort option (optional).

    Returns:
        TemplateResponse: The rendered HTML response with more flight results.
    """
    
    search = Search(
        departure=departure,
        destination=destination,
        departure_date=departure_date,
        return_date=return_date,
    )

    stops = None if stops == "None" else stops
    filters = Filters(stops=stops, airlines=airlines)
    sort_option = SortOption(sort)
    flights_data = get_flights_filter_and_sort(search, filters, sort_option)

    response = templates.TemplateResponse(
        "partials/search-flights/more-results.html",
        {
            "request": request,
            "moreFlights": flights_data[20:],
        },
    )

    return response