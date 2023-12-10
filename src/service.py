from src.const import CSV_PATH
from src.locate_restaurants import RestaurantFinder
from src.models.restaurants import read_csv
from decimal import Decimal
from abc import ABC, abstractmethod


class BaseService(ABC):

    @abstractmethod
    def run(self):
        pass


class NearRestaurantService(BaseService):

    def __init__(self, latitude: str, longitude: str):
        self.latitude = latitude
        self.longitude = longitude

    def run(self) -> dict:
        restaurants = read_csv(CSV_PATH)

        finder = RestaurantFinder(restaurants)
        near_restaurant = finder.find_nearby_restaurants(
            target_latitude=Decimal(self.latitude),
            target_longitude=Decimal(self.longitude)
        )

        return {
            'success': True,
            'restaurants': [restaurant.dict() for restaurant in near_restaurant]
        }
