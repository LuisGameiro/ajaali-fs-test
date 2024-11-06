from typing import List
from ajaali.models.flight import Flight
from ajaali.models.search import SortOption, default_sort


def sort_flights(flight_list, sort_option: SortOption = default_sort) -> List[Flight]:
    """
    Sorts flights based on the provided sorting option.

    Parameters:
        flight_list (List[Flight]): The list of flights to sort.
        sort_option (SortOption): The sorting option to apply.

    Returns:
        Tuple: A tuple containing the sorted flights and the sort option.
    """

    sort_key = {
        SortOption.TOP_FLIGHTS: lambda x: (x["arrival_dt"] - x["departure_dt"]).total_seconds()*float(x["price"]),
        SortOption.PRICE: lambda x: x["price"],
        SortOption.DEPARTURE_TIME: lambda x: x["departure_dt"],
        SortOption.ARRIVAL_TIME: lambda x: x["arrival_dt"],
        SortOption.DURATION: lambda x: (x["arrival_dt"] - x["departure_dt"]),
        SortOption.EMISSIONS: lambda x: x["emissions"],
    }.get(sort_option)

    return sorted(flight_list, key=sort_key)
