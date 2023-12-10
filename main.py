from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.service import NearRestaurantService
from src.schemas import RestaurantsResponseSchema

app = FastAPI(
    title="Restaurants API"
)


@app.get('/restaurants/', response_model=RestaurantsResponseSchema)
def get_near_restaurants(latitude: str, longitude: str) -> JSONResponse:
    service = NearRestaurantService(latitude, longitude)
    data = service.run()
    return JSONResponse(content=data, status_code=200)
