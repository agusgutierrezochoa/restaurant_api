import pytest
from src.models.restaurants import Restaurant
from decimal import Decimal


@pytest.fixture
def create_restaurant():

    def _create(
        id=1,
        latitude=Decimal(-32.88503849771821),
        longitude=Decimal(-68.85516058564684),
        availability_radius=4,
        open_hour='19:00',
        close_hour='23:00',
        rating=5,
    ):
        return Restaurant(
            id=id,
            latitude=latitude,
            longitude=longitude,
            availability_radius=availability_radius,
            open_hour=open_hour,
            close_hour=close_hour,
            rating=rating
        )

    return _create


@pytest.fixture
def csv_file_content():
    # Example CSV content for testing
    return "id,latitude,longitude,availability_radius,open_hour,close_hour,rating \n" \
        "1,-32.88503849771821,-68.85516058564684,4,19:00,23:00,5"
