class Crop():
    def __init__(self, expected_performance, min_precipitation, max_precipitation, start_season, end_season):
        self.area = 0.0 # m2
        self.total_accumulated_precipitation = 0.0 # mm
        self.expected_performance = expected_performance # Kg/m2
        self.min_precipitation = min_precipitation
        self.max_precipitation = max_precipitation
        self.start_season = start_season
        self.end_season = end_season
        # TODO: altitude, ground_type, temperature
    
    def calculate_area(self, coordinates):
        pass

    # def calculate_total_accumulated_precipitation(self, year):
    #     pass

    def suggest_seeding(self):
        pass
