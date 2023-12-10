import pytest
from src.locate_restaurants import RestaurantFinder
from datetime import datetime
from decimal import Decimal
import pytz

now = datetime(2023, 1, 1, 15, 0)


class TestRestaurantFinder:

    @pytest.mark.parametrize(
        "open_hour,close_hour,now,expected_result",
        [
            ("11:00", "21:00", datetime(2023, 12, 9, 15, 30, 0), True),
            ("20:00", "23:00", datetime(2023, 12, 9, 21, 12, 12), True),
            ("20:00", "22:00", datetime(2023, 12, 9, 19, 59, 12), False),
            ("19:00", "02:00", datetime(2023, 12, 9, 17, 0, 0), False),
            ("19:00", "02:00", datetime(2023, 12, 9, 22, 0, 0), True),
            ("19:00", "02:00", datetime(2023, 12, 10, 1, 0, 0), True),
            ("19:00", "02:00", datetime(2023, 12, 10, 3, 0, 0), False),
        ]
    )
    def test_is_restaurant_open(
        self,
        open_hour,
        close_hour,
        now,
        expected_result
    ):
        finder = RestaurantFinder([])

        result = finder.is_restaurant_open(
            open_hour,
            close_hour,
            now
        )
        assert expected_result == result

    @pytest.mark.freeze_time(now)
    @pytest.mark.parametrize(
        "latitude,longitude,timezone",
        [
            (
                Decimal(-32.88600760225919),
                Decimal(-68.85612322260924),
                pytz.timezone('America/Argentina/Mendoza')
            ),
            (
                Decimal(40.74744954444959),
                Decimal(-74.00044261376411),
                pytz.timezone('America/New_York')
            )
        ]
    )
    def test_get_now_in_timezone(
        self,
        latitude,
        longitude,
        timezone
    ):
        expected_result = datetime.now(timezone)
        finder = RestaurantFinder([])

        timezone_result = finder.get_now_in_timezone(
            latitude=latitude,
            longitude=longitude
        )

        assert expected_result == timezone_result

    @pytest.mark.freeze_time(now)
    def test_find_nearby_restaurants_near_closed_restaurant(
        self,
        create_restaurant
    ):
        near_coordinates = (Decimal(-32.88678218746367), Decimal(-68.85337561002584))
        r1 = create_restaurant(
            id=1,
            latitude=Decimal(-32.88627675597903),
            longitude=Decimal(-68.8562659068129),
        )

        finder = RestaurantFinder([r1])
        restaurants = finder.find_nearby_restaurants(
            near_coordinates[0],
            near_coordinates[1]
        )

        assert restaurants == []

    @pytest.mark.freeze_time(now)
    def test_find_nearby_restaurants_near_open_restaurant(
        self,
        create_restaurant
    ):
        near_coordinates = (Decimal(-32.88678218746367), Decimal(-68.85337561002584))
        r1 = create_restaurant(
            id=1,
            latitude=Decimal(-32.88627675597903),
            longitude=Decimal(-68.8562659068129),
            open_hour="11:00"
        )

        finder = RestaurantFinder([r1])
        restaurants = finder.find_nearby_restaurants(
            near_coordinates[0],
            near_coordinates[1]
        )

        assert restaurants == [r1]

    @pytest.mark.freeze_time(now)
    def test_find_nearby_restaurants_far_open_restaurant(
        self,
        create_restaurant
    ):
        far_coordinates = (Decimal(-34.581582543816936), Decimal(-58.441774139019074))
        r1 = create_restaurant(
            id=1,
            latitude=Decimal(-32.88627675597903),
            longitude=Decimal(-68.8562659068129),
            open_hour="11:00"
        )
        finder = RestaurantFinder([r1])
        restaurants = finder.find_nearby_restaurants(
            far_coordinates[0],
            far_coordinates[1]
        )

        assert restaurants == []
