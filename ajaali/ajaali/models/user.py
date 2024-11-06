from pydantic import BaseModel

class User(BaseModel):
    username: str

user_example = {"username": "Sara"}
