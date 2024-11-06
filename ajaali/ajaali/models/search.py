from datetime import date, timedelta
from enum import Enum
from pydantic import BaseModel, Field
from typing import List

class SortOption(str, Enum):
    TOP_FLIGHTS = "Top flights"
    PRICE = "Price"
    DEPARTURE_TIME = "Departure time"
    ARRIVAL_TIME = "Arrival time"
    DURATION = "Duration"
    EMISSIONS = "Emissions"

default_sort = SortOption.TOP_FLIGHTS

class Filters(BaseModel):
    stops: int|None = Field(None, description="Number of stops")
    airlines: List[str] = Field([], description="List of preferred airlines")
    bags: int|None = Field(None, description="Number of bags")
    price: int|None = Field(None, description="Maximum price")
    emissions: int|None = Field(None, description="Maximum emissions")
    connecting_airports: List[str] = Field([], description="Preferred connecting airports")
    duration: timedelta|None = Field(None, description="Maximum duration")

default_filters = Filters()

class Search(BaseModel):
    departure: str = Field("", description="Departure location")
    destination: str = Field("", description="Destination location")
    departure_date: date = Field(date.today(), description="Departure date and time")
    return_date: date = Field(date.today() + timedelta(days=1), description="Return date and time")
    flight_type: str = Field("Round trip", description="Type of trip")
    passengers: int = Field(1, description="Number of passengers")
    flight_class: str = Field("Economy", description="Class of flight")

default_search = Search()
