from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_world/")
def read_root():
    return {"Hello": "World"}
