# Restaurant API

Welcome to the Restaurant Locator API! This API allows you to find nearby restaurants based on specific coordinates. Simply make a request to the endpoint with the desired latitude and longitude, and the API will return a list of restaurants in the vicinity.

## Getting started

First of all, you'll need to clone this repository to your local machine by doing:

    git@github.com:GH_USER/restaurant_api.git
Then move to the root of the project and start the server:

    cd restaurant_api
    docker-compose up --build
After that, once you have the server up and running you'll be able to request the restaurant api:

    curl -XGET "http://localhost:8080/restaurants/?latitude=-32.886229955082314&longitude=-68.85629382073354" | jq
If you need to update the CSV file, feel free to modify the `restaurants_list.csv` located in the root of the project ( `/restaurant_api` )

## Documentation
The api was documented using FastAPI auto documenting. If you want to check the requests/responses, you'll have to go to:

    http://localhost:8080/docs

## Testing
In order to run tests, you'll have to exec the docker container and the run pytest:

    docker exec -it <id_of_the_container> sh
    # pytest test/
(You can find the id_of_the_container by running `docker ps`
## Contributing
If you want to contribute to this repository, you'll need to create a PR, with all the CI checks passed and wait for an approval. 