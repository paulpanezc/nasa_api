from bs4 import BeautifulSoup
import requests


stations = {
    "CO": {
        "state": "REAL"
    },
    "EMA": {
        "state": "AUTOMATICA"
    }
}


class SenamhiHelper():
    def __init__(self, period, station_code, station_type):
        self.period = period
        self.station_code = station_code
        self.station_type = station_type

    def get_measurements(self, table):
        measurements = []
        i = 0
        for row in table("tr"):
            measurement = {}
            print("-"*117)
            print(row)
            print("-"*117)
            if i > 1:
                if self.station_type == "CO":
                    measurement["date"] = row("td")[0].text.strip()
                    measurement["max_temperature"] = row("td")[1].text.strip()
                    measurement["min_temperature"] = row("td")[2].text.strip()
                    measurement["humidity"] = row("td")[3].text.strip()
                    measurement["precipitation"] = row("td")[4].text.strip()
                elif self.station_type == "EMA":
                    measurement["date"] = row("td")[0].text.strip()
                    measurement["hour"] = row("td")[1].text.strip()
                    measurement["temperature"] = row("td")[2].text.strip()
                    measurement["precipitation"] = row("td")[3].text.strip()
                    measurement["humidity"] = row("td")[4].text.strip()
                    measurement["wind_direction"] = row("td")[5].text.strip()
                    measurement["wind_velocity"] = row("td")[6].text.strip()
                measurements.append(measurement)
            i += 1
        return measurements
    
    def get_station_info(self):
        # TODO: &soloAlt=3363
        url = "https://www.senamhi.gob.pe/mapas/mapa-estaciones-2/export.php?CBOFiltro={}&estaciones={}&t_e=M&estado={}&" \
                "cod_old=&cate_esta={}".format(self.period, self.station_code, stations[self.station_type]["state"], self.station_type)
        senamhi_response = requests.get(url)
        senamhi_data = senamhi_response.text
        data_scraping = BeautifulSoup(senamhi_data, "html.parser")
        data_table = data_scraping("table")[0]
        measurements_table = data_scraping("table")[1]
        station_info = {
            "station_name": data_table("tr")[0].text.strip().split(" : ")[1],
            "region": data_table("tr")[1]("td")[1].text,
            "province": data_table("tr")[1]("td")[3].text,
            "district": data_table("tr")[1]("td")[5].text,
            "latitude": data_table("tr")[2]("td")[1].text,
            "longitude": data_table("tr")[2]("td")[3].text,
            "altitude": data_table("tr")[2]("td")[5].text,
            "station_type": data_table("tr")[3]("td")[1].text,
            "station_code": data_table("tr")[3]("td")[3].text,
            "measurements": self.get_measurements(measurements_table)
        }
        return station_info
