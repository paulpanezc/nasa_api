from shapely.geometry import Polygon
# from geopy.distance import geodesic


PRODUCTS = [
    {
        "name": "quinoa",
        "min_temperature_required": 15,
        "max_temperature_required": 25,
        "min_precipitation_required": 300,
        "max_precipitation_required": 600,
        # "min_ph_required": 6,
        # "max_ph_required": 8.5,
        # "min_altitude_required": "",
        # "max_altitude_required": "",
        # "min_solar_radiation_required": "",
        # "max_solar_radiation_required": "",
        # "min_wind_speed_required": "",
        # "max_wind_speed_required": ""
    }
]


class CropService():
    def __init__(self, product_name, coordinates):
        self.product_name = product_name
        self.area = 0.0 # m2
        self.total_accumulated_precipitation = 0.0 # mm
        self.projected_min_temperature = 0.0
        self.projected_max_temperature = 0.0
        self.expected_performance = 0.00 # Kg/ha
        self.coordinates = coordinates

    def calculate_area(self):
        polygon = Polygon(self.coordinates)
        return polygon.area
    
    def get_start_season(self):
        pass

    def get_end_season(self):
        pass

    def get_climatic_parameter(self, parameter_name):
        for product in PRODUCTS:
            if product["name"] == self.product_name:
                return product[parameter_name]
        return None

    def get_min_temperature_required(self):
        return self.get_climatic_parameter("min_temperature_required")
    
    def get_max_temperature_required(self):
        return self.get_climatic_parameter("max_temperature_required")
    
    def get_min_precipitation_required(self):
        return self.get_climatic_parameter("min_precipitation_required")
    
    def get_max_precipitation_required(self):
        return self.get_climatic_parameter("max_precipitation_required")
    
    # def get_min_altitude_required(self):
    #     return self.get_climatic_parameter("get_min_altitude_required")
    
    # def get_max_altitude_required(self):
    #     return self.get_climatic_parameter("get_max_altitude_required")
    
    def is_available(self):
        # alpha = 0.3
        # beta = 0.7
        # gamma = 2.0
        # return alpha * self.area + beta * self.total_accumulated_precipitation - gamma
        if self.total_accumulated_precipitation >= self.get_min_precipitation_required() and \
            self.total_accumulated_precipitation <= self.get_max_precipitation_required() and \
            self.projected_max_temperature >= self.get_min_temperature_required() and \
            self.projected_min_temperature <= self.get_max_temperature_required():
            return True
        return False

