from typing import List
from ajaali.models.flight import Flight
from ajaali.models.search import (
    Filters,
    default_filters,
)


def filter_flights(flight_list, filters: Filters = default_filters) -> List[Flight]:
    """
    Filters flights based on the provided filters.

    Parameters:
        flight_list (List[Flight]): The list of flights to filter.
        filters (Filters): The filters to apply.

    Returns:
        Tuple: A tuple containing the filtered flights and the updated filters.
    """
    
    filtered_flights = flight_list

    if filters.stops is not None:
        filtered_flights = [
            flight
            for flight in flight_list
            if flight["number_of_stops"] <= filters.stops
        ]

    if filters.airlines:
        filtered_flights = [
            flight
            for flight in filtered_flights
            if flight["airline"] in filters.airlines
        ]

    return filtered_flights
