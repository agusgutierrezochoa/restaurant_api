from rtree import index
from concurrent.futures import ThreadPoolExecutor, as_completed
from geopy.distance import geodesic
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz
from decimal import Decimal


class RestaurantFinder:

    def __init__(self, restaurants: list):
        self.restaurants = restaurants
        self.idx = self.build_spatial_index

    def build_spatial_index(self) -> index.Index:
        idx = index.Index()
        for i, restaurant in enumerate(self.restaurants):
            idx.insert(i, (restaurant.latitude, restaurant.longitude, restaurant.latitude, restaurant.longitude))
        return idx

    def find_nearby_restaurants(
        self,
        target_latitude: float,
        target_longitude: float
    ) -> list:
        target_location = (target_latitude, target_longitude)
        nearby_restaurants = []

        def calculate_distance(restaurant):
            restaurant_location = (restaurant.latitude, restaurant.longitude)
            return geodesic(target_location, restaurant_location).kilometers

        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(calculate_distance, restaurant): restaurant for restaurant in self.restaurants}
            for future in as_completed(futures):
                restaurant = futures[future]
                try:
                    distance = future.result()
                    if (
                        distance <= restaurant.availability_radius and
                        self.is_restaurant_open(
                            open_hour=restaurant.open_hour,
                            close_hour=restaurant.close_hour,
                            now=self.get_now_in_timezone(target_latitude, target_longitude)
                        )
                    ):
                        nearby_restaurants.append(restaurant)
                except Exception as e:
                    print(f"Error calculating distance for {restaurant.id}: {e}")

        return nearby_restaurants

    def get_now_in_timezone(
        self,
        latitude: Decimal,
        longitude: Decimal
    ) -> datetime:
        tz_finder = TimezoneFinder()
        timezone_str = tz_finder.timezone_at(lat=latitude, lng=longitude)
        if timezone_str:
            return datetime.now(pytz.timezone(timezone_str))
        # Just return now in UTC
        return datetime.now()

    def is_restaurant_open(
        self,
        open_hour: str,
        close_hour: str,
        now: datetime
    ) -> bool:
        open_hour = datetime.strptime(open_hour, "%H:%M").time()
        close_hour = datetime.strptime(close_hour, "%H:%M").time()

        current_time = now.time()

        if close_hour < open_hour:
            return open_hour <= current_time or current_time <= close_hour
        else:
            return open_hour <= current_time <= close_hour
