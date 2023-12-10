import csv
from concurrent.futures import ProcessPoolExecutor
from pydantic import BaseModel


class Restaurant(BaseModel):
    id: int
    latitude: float
    longitude: float
    availability_radius: float
    open_hour: str
    close_hour: str
    rating: float


def parse_csv_row(row: any) -> Restaurant:
    return Restaurant(
        id=int(row[0]),
        latitude=float(row[1]),
        longitude=float(row[2]),
        availability_radius=float(row[3]),
        open_hour=str(row[4]),
        close_hour=str(row[5]),
        rating=float(row[6])
    )


def read_csv(file_path: str) -> list:
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        data = list(csv_reader)

    with ProcessPoolExecutor(max_workers=4) as executor:
        restaurants = list(executor.map(parse_csv_row, data))

    return restaurants
