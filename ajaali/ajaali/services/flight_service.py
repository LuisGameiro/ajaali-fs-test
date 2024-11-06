from datetime import date
from typing import List
from ajaali.database.flights import add_flights, get_flights
from ajaali.fullstack_test.flight_data_generator import flight_data
from ajaali.models.flight import Flight
from ajaali.utils.sort import sort_flights
from ajaali.utils.filters import filter_flights
from ajaali.models.search import SortOption, Filters, Search


def cheat_get_flights_and_populate_table(
    departure: str,
    destination: str,
    departure_date: date,
    return_date: date,
) -> list[Flight]:
    """
    Retrieve flights and populate table if needed.

    Parameters:
    - departure (str): The departure location of the flights.
    - destination (str): The destination location of the flights.
    - departure_date (date): The departure date of the flights.

    - return_date (date): The return date of the flights.

    Returns:
    - list (Flight): Response a list of flight data or empty in case of error.
    """
    try:
        flights = get_flights(
            departure,
            destination,
            departure_date,
            return_date,
        )

        flights = flights["data"]
        if len(flights) > 50:
            return flights

        else:
            add_flights(
                flight_data(departure, destination, departure_date, return_date)
            )
            new_flights = get_flights(
                departure, destination, departure_date, return_date
            )

            return new_flights["data"]
    except Exception:
        return []


def get_flights_filter_and_sort(
    search: Search, filters: Filters, sort_option: SortOption
) -> List[Flight]:
    """
    Fetch flights, apply filters, and sort them based on the specified options.

    Args:
        search (Search): Search criteria including departure, destination, destination, dates.
        filters (Filters): The filter criteria.
        sort_option (SortOption): The sorting option.

    Returns:
        List[Flight]: A list of sorted and filtered flights.
    """

    flights_data = cheat_get_flights_and_populate_table(
        search.departure, search.destination, search.departure_date, search.return_date
    )

    flights_filter = filter_flights(flights_data, filters)

    flights_sorted = sort_flights(flights_filter, sort_option)

    return flights_sorted
