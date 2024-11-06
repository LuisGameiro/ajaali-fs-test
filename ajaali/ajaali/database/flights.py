from ajaali.utils.converter import convert_app_dynamo, convert_dynamo_app
from .db import dynamodb
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from datetime import date
from ajaali.models.flight import Flight

table = dynamodb.Table("FlightsTable")


def add_flight(flight: Flight) -> dict:
    """
    Add a single flight to the DynamoDB table.

    Parameters:
    - flight (Flight): The flight data to be added.

    Returns:
    - dict: Response object with a flight data or error message.
    """
    try:
        item = convert_app_dynamo(flight)
        table.put_item(Item=item)

        return {"status": "success", "data": flight}
    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        return {"status": "error", "message": f"Failed to add flight: {error_message}"}


def add_flights(flights: list[Flight]) -> dict:
    """
    Add multiple flights to the DynamoDB table.

    Parameters:
    - flights (list): A list of flight data dictionaries to be added.

    Returns:
    - dict: Response object with a list of flight data or error message.
    """
    try:
        for flight in flights:
            add_flight(flight)

        return {"status": "success", "data": flights}
    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        return {"status": "error", "message": f"Failed to add flights: {error_message}"}


def get_flight(flight_id: str) -> dict:
    """
    Retrieve a single flight from the DynamoDB table by flight_id.

    Parameters:
    - flight_id (str): The ID of the flight to retrieve.

     Returns:
    - dict: Response object with a flight data or error message.
    """
    try:
        response = table.query(KeyConditionExpression=Key("flight_id").eq(flight_id))
        if not response["Items"]:
            raise {
                "status": "error",
                "message": "Failed to retrieve flight: Flight not found",
            }

        return {"status": "success", "data": response["Items"][0]}
    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        return {
            "status": "error",
            "message": f"Failed to retrieve flight: {error_message}",
        }


def get_flights(
    departure: str, destination: str, departure_date: date, return_date: date
) -> dict:
    """
    Retrieve flights from DynamoDB table based on departure, destination, and departure date.

    Parameters:
    - departure (str): The departure location of the flights.
    - destination (str): The destination location of the flights.
    - departure_date (date): The departure date of the flights.
    - return_date (date): The return date of the flights.

    Returns:
    - dict: Response object with a list of flight data or error message.

    Note:
    we dont look for the return date due too that it was something that was not being taken in account on the front end example
    """
    departure_date_str = departure_date.strftime("%Y-%m-%d")
    try:
        response = table.query(
            IndexName="source-departure-index",
            KeyConditionExpression=Key("source").eq(departure)
            & Key("departure_dt").begins_with(departure_date_str),
            FilterExpression=Attr("sink").eq(destination),
        )
        results = [convert_dynamo_app(flight) for flight in response.get("Items", [])]

        return {"status": "success", "data": results}
    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        return {
            "status": "error",
            "message": f"Failed to retrieve flights: {error_message}",
        }
