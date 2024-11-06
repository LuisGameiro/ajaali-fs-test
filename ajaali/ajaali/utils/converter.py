import uuid
from datetime import datetime
from decimal import Decimal
from ajaali.models.flight import Flight


def convert_dynamo_app(flight_data: dict) -> Flight:
    """
    Convert DynamoDB flight data to application-readable format.

    Parameters:
    - flight_data (dict): The dictionary containing flight data from DynamoDB.

    Returns:
    - dict: A dictionary with converted flight data.
    """
    return {
        "airline": flight_data["airline"],
        "arrival_dt": datetime.strptime(flight_data["arrival_dt"], "%Y-%m-%dT%H:%M:%S"),
        "departure_dt": datetime.strptime(
            flight_data["departure_dt"], "%Y-%m-%dT%H:%M:%S"
        ),
        "emissions": flight_data["emissions"],
        "number_of_stops": flight_data["number_of_stops"],
        "price": Decimal(flight_data["price"]),
        "sink": flight_data["sink"],
        "source": flight_data["source"],
    }


def convert_app_dynamo(flight_data: Flight) -> dict:
    """
    Convert application flight data to DynamoDB-readable format.

    Parameters:
    - flight_data (Flight): The dictionary containing flight data from the application.

    Returns:
    - dict: A dictionary with converted flight data.
    """
    return {
        "flight_id": generate_flight_id(),
        "airline": flight_data["airline"],
        "arrival_dt": flight_data["arrival_dt"].isoformat(),
        "departure_dt": flight_data["departure_dt"].isoformat(),
        "emissions": flight_data["emissions"],
        "number_of_stops": flight_data["number_of_stops"],
        "price": str(flight_data["price"]),
        "sink": flight_data["sink"],
        "source": flight_data["source"],
    }


def generate_flight_id() -> str:
    """
    Generate a unique flight ID.

    Returns:
    - str: A unique flight ID string.
    """
    return str(uuid.uuid4())
