from urllib.parse import urlencode
from fastapi import Request
from ajaali.models.search import Filters, Search, SortOption


def build_new_url(request: Request, search:Search,filters:Filters,sort:SortOption) -> str:
    """
    Build a new URL with the given parameters and optional query parameters.

    Returns:
        str: The newly constructed URL.
    """
    base_url = str(request.url)
    new_url = f"{base_url}/{search.departure}/{search.destination}/{str(search.departure_date).split(' ')[0]}/{str(search.return_date).split(' ')[0]}"
    
    query_params = {}
    if filters.stops:
        query_params['stops'] = filters.stops
    if filters.airlines:
        query_params['airlines'] = ",".join(filters.airlines)
    if sort:
        query_params['sort'] = sort

    if query_params:
        new_url = f"{new_url}?{urlencode(query_params)}"

    return new_url