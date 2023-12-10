import pytest
from src.models.restaurants import Restaurant


@pytest.fixture
def create_restaurant(
    id,
    latitude,
    longitude,
    availability_radius,
    open_hour,
    close_hour,
    rating,
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
