import requests


class NasaService():
    def __init__(self):
        pass

    def calculate_total_accumulated_precipitation(self, year, latitude, longitude):
        # Doc: https://power.larc.nasa.gov/api/pages/?urls.primaryName=Daily
        url = f"https://power.larc.nasa.gov/api/projection/daily/point?start={year}0101& \
                end={year}1231&latitude={latitude}&longitude={longitude}&community=ag&parameters=PRECTOTCORR"
        response = requests.get(url)
        nasa_data = response.text
        precipitation = 0.0
        for measure in nasa_data["properties"]["parameter"]["PRECTOTCORR"]:
            precipitation += measure[measure.keys()[0]]
        return precipitation // 365

