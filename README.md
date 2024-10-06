# API to provide climatic data from NASA for App QuinuaEstellar - Team Rocket NASA Challenge Junin 2024

### System requirements
- python 3.12.3
- poetry 1.8.3
- beautifulsoup4
- requests
- fastapi[standard]
- uvicorn[standard]

### Use

> poetry install --no-root

> fastapi dev main.py

### Deploy

> Connect Github project in Render.com

> Enviroment variable in Render.com:

- PORT

> Build command in Render.com settings

- pip install -r requirements.txt

- uvicorn main:app --host 0.0.0.0 --port $PORT

### Use API in production

> https://nasa-api-8mvu.onrender.com/api/rocket/availability?product_name=quinoa&start_season_datetime=2025-11-01&coordinates=[{"latitude":"-12.047217541937576","longitude":"-75.19885024051018"}, {"latitude":"-12.047162456079048","longitude":"-75.1987456343586"}, {"latitude":"-12.047260823675632","longitude":"-75.19864773372956"}, {"latitude":"-12.047325090485925","longitude":"-75.19877916197129"}]

### Future implementations

> Incorporate SOILS API to get data like nitrogen or phh2o

- URL: https://rest.isric.org/soilgrids/v2.0/properties/query?lat=-11.7364166&lon=-75.4432235&parameters=["nitrogen","phh2o"]
