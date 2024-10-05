FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

COPY team_league/service/requirements.txt ./

RUN pip install -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY team_league $APP_HOME/team_league
EXPOSE 8080
CMD ["uvicorn", "team_league.service.main:app", "--port", "8080"]
