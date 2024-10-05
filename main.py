from typing import Union

from fastapi import FastAPI

from services.senamhi_service import SenamhiService
from services.nasa_service import NasaService

# import uvicorn
# import os


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
    service = SenamhiService(period, station_code, station_type)
    return service.get_station_info()


@app.get("/nasa/precipitation")
def senamhi(year: str, latitude: str, longitude: str):
    service = NasaService()
    return service.calculate_total_accumulated_precipitation(year, latitude, longitude)


# if __name__ == "__main__":
#     uvicorn.run(app, debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
