import requests
import json


PARAMETERS = {
    "total_accumulated_precipitation": "PRECTOTCORR",
    "average_min_temperature": "T2M_MIN",
    "average_max_temperature": "T2M_MAX",
    # "average_max_radiation_solar": "ALLSKY_SFC_SW_DNI",
    # "average_max_wind_velocity": "WS2M_MAX"
}


class NasaService():
    def __init__(self, start_season, end_season, latitude, longitude):
        self.start_season = start_season
        self.end_season = end_season
        self.latitude = latitude
        self.longitude = longitude

    def get_measurements(self, parameter_name):
        nasa_parameter = PARAMETERS[parameter_name]
        # Doc: https://power.larc.nasa.gov/api/pages/?urls.primaryName=Climate%20Projection
        url = f"https://power.larc.nasa.gov/api/projection/daily/point?start={self.start_season}&end={self.end_season}&latitude={self.latitude}&longitude={self.longitude}&community=ag&parameters={nasa_parameter}"
        response = requests.get(url)
        measurements_data = json.loads(response.text)["properties"]["parameter"][nasa_parameter]
        return measurements_data


    def calculate_total_accumulated_precipitation(self):
        measurements_data = self.get_measurements("total_accumulated_precipitation")
        precipitation = 0.0
        for measure in measurements_data:
            precipitation += measurements_data[measure]
        return precipitation

    def calculate_average_min_temperature(self):
        measurements_data = self.get_measurements("average_min_temperature")
        min_temperature = 0.0
        days = 0
        for measure in measurements_data:
            min_temperature += measurements_data[measure]
            days += 1
        if days > 0:
            return min_temperature // days
        return min_temperature

    def calculate_average_max_temperature(self):
        measurements_data = self.get_measurements("average_max_temperature")
        max_temperature = 0.0
        days = 0
        for measure in measurements_data:
            max_temperature += measurements_data[measure]
            days += 1
        if days > 0:
            return max_temperature // days
        return max_temperature
    
    # def calculate_average_max_radiation_solar(self):
    #     measurements_data = self.get_measurements("average_max_radiation_solar")
    #     max_radiation_solar = 0.0
    #     for measure in measurements_data:
    #         max_radiation_solar += measurements_data[measure]
    #     return max_radiation_solar // 365
    
    # def calculate_average_max_wind_velocity(self):
    #     measurements_data = self.get_measurements("average_max_radiation_solar")
    #     max_radiation_solar = 0.0
    #     for measure in measurements_data:
    #         max_radiation_solar += measurements_data[measure]
    #     return max_radiation_solar // 365

