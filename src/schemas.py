from pydantic import BaseModel
from typing import List
from src.models.restaurants import Restaurant


class RestaurantsResponseSchema(BaseModel):
    success: bool
    restaurants: List[Restaurant]
