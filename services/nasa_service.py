import requests
import json


class NasaService():
    def __init__(self):
        pass

    def calculate_total_accumulated_precipitation(self, year, latitude, longitude):
        # Doc: https://power.larc.nasa.gov/api/pages/?urls.primaryName=Daily
        url = f"https://power.larc.nasa.gov/api/projection/daily/point?start={year}0101&end={year}1231&latitude={latitude}&longitude={longitude}&community=ag&parameters=PRECTOTCORR"
        response = requests.get(url)
        measurements_data = json.loads(response.text)["properties"]["parameter"]["PRECTOTCORR"]
        precipitation = 0.0
        for measure in measurements_data:
            precipitation += measurements_data[measure]
        return precipitation // 365

    def calculate_average_min_temperature(self, year, latitude, longitude):
        # Doc: https://power.larc.nasa.gov/api/pages/?urls.primaryName=Daily
        url = f"https://power.larc.nasa.gov/api/projection/daily/point?start={year}0101&end={year}1231&latitude={latitude}&longitude={longitude}&community=ag&parameters=T2M_MIN"
        response = requests.get(url)
        measurements_data = json.loads(response.text)["properties"]["parameter"]["T2M_MIN"]
        min_temperature = 0.0
        for measure in measurements_data:
            min_temperature += measurements_data[measure]
        return min_temperature // 365

    def calculate_average_max_temperature(self, year, latitude, longitude):
        # Doc: https://power.larc.nasa.gov/api/pages/?urls.primaryName=Daily
        url = f"https://power.larc.nasa.gov/api/projection/daily/point?start={year}0101&end={year}1231&latitude={latitude}&longitude={longitude}&community=ag&parameters=T2M_MAX"
        response = requests.get(url)
        measurements_data = json.loads(response.text)["properties"]["parameter"]["T2M_MAX"]
        max_temperature = 0.0
        for measure in measurements_data:
            max_temperature += measurements_data[measure]
        return max_temperature // 365

