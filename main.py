from datetime import datetime

from typing import Union

from fastapi import FastAPI

# from services.senamhi_service import SenamhiService
from services.nasa_service import NasaService
from services.crop_service import CropService

# import uvicorn
# import os

import json


app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.get("/nasa/indicators/")
# def nasa_indicators(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.get("/nasa/climatic/")
# def nasa_climatic(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.get("/senamhi/")
# def senamhi(period: str, station_code: str, station_type: str):
#     service = SenamhiService(period, station_code, station_type)
#     return service.get_station_info()


# @app.get("/nasa/precipitation")
# def senamhi(year: str, latitude: str, longitude: str):
#     service = NasaService()
#     return service.calculate_total_accumulated_precipitation(year, latitude, longitude)


@app.get("/api/rocket/availability")
def rocket(product_name: str, start_season_datetime: datetime, end_season_datetime: datetime, coordinates: Union[str, None] = None):
    start_season = start_season_datetime.strftime("%Y%m%d")
    end_season = end_season_datetime.strftime("%Y%m%d")
    list_coordinates = json.loads(coordinates)
    crop = CropService(product_name, coordinates)
    # crop.area = crop.calculate_area()
    climatic = NasaService(start_season, end_season, float(list_coordinates[0]["latitude"]), float(list_coordinates[0]["longitude"]))
    crop.total_accumulated_precipitation = climatic.calculate_total_accumulated_precipitation()
    crop.projected_min_temperature = climatic.calculate_average_min_temperature()
    crop.projected_max_temperature = climatic.calculate_average_max_temperature()
    
    response = {
        "start_season": start_season_datetime,
        "end_season": end_season_datetime,
        "total_acumulated_precipitation": f"{crop.total_accumulated_precipitation} mm",
        "average_min_temperature": f"{crop.projected_min_temperature} °C",
        "average_max_temperature": f"{crop.projected_max_temperature} °C"
    }
    
    if crop.is_available():
        response["message"] = "Under climatic projected conditions it is suggested to seed quinoa in that location and season"
    else:
        response["message"] = "Under climatic projected conditions it is not suggested to seed quinoa in that location and season."
    
    return response


# if __name__ == "__main__":
#     uvicorn.run(app, debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
