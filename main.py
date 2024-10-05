from typing import Union

from fastapi import FastAPI

from helpers.senamhi_helper import SenamhiHelper

import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/nasa/indicators/")
def nasa_indicators(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/nasa/climatic/")
def nasa_climatic(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/senamhi/")
def senamhi(period: str, station_code: str, station_type: str):
    helper = SenamhiHelper(period, station_code, station_type)
    return helper.get_station_info()


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
