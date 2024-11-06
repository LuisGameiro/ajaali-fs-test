from pydantic import BaseModel,Field
from datetime import datetime
from decimal import Decimal

class Flight(BaseModel):
    arrival_dt: datetime = Field(..., description="Arrival date and time")
    departure_dt: datetime = Field(..., description="Departure date and time")
    source: str = Field(..., description="Departure location")
    sink: str = Field(..., description="Arrival location")
    airline: str = Field(..., description="Airline name")
    emissions: int = Field(..., description="Carbon emissions")
    number_of_stops: int = Field(..., description="Number of stops")
    price: Decimal = Field(..., description="Ticket price")
 