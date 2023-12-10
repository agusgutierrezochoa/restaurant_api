import pytest
from src.locate_restaurants import RestaurantFinder
from datetime import datetime


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
        # import ipdb; ipdb.set_trace(context=20)
        assert expected_result == result
