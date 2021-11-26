from datetime import datetime
from pathlib import Path
import json
from time import sleep
import requests  # type: ignore
import sqlalchemy.exc
from sqlalchemy import create_engine
from datetime import date
import psycopg2
import dags.configinc as config


def _data_amzn():
    end_point = f"{config.end_point_amzn_pop}"
    print(f"Getting data from Amazon {end_point}...")
    r = requests.get(end_point)
    data_amzn = r.json()

    with open(f"/tmp/{config.SYMBOL_AMZN}.json", "w") as f:
        json.dump(data_amzn, f)


def _insert_amzn():
    with open(f"/tmp/{config.SYMBOL_AMZN}.json", "r") as f:
        data_amzn = json.load(f)

    for date_str, day in data_amzn["Time Series (Daily)"].items():
        date = datetime.strptime(date_str, "%Y-%m-%d")
        open_ = float(day["1. open"])
        high = float(day["2. high"])
        low = float(day["3. low"])
        close = float(day["4. close"])
        volume = int(day["5. volume"])

        SQL_INSERT = f"""
        INSERT INTO prices_from_agm (date, Symbol, open, high, low, close, volume)
        VALUES ('{date}', '{config.SYMBOL_AMZN}', {open_}, {high}, {low}, {close}, {volume})
        """
        result = config.engine.execute(SQL_INSERT)
        result.close()


def _data_goog():
    end_point = f"{config.end_point_goog_pop}"
    print(f"Getting data from Google {end_point}...")
    r = requests.get(end_point)
    data_goog = r.json()

    with open(f"/tmp/{config.SYMBOL_GOOG}.json", "w") as f:
        json.dump(data_goog, f)


def _insert_goog():
    with open(f"/tmp/{config.SYMBOL_GOOG}.json", "r") as f:
        data_goog = json.load(f)

    for date_str, day in data_goog["Time Series (Daily)"].items():
        date = datetime.strptime(date_str, "%Y-%m-%d")
        open_ = float(day["1. open"])
        high = float(day["2. high"])
        low = float(day["3. low"])
        close = float(day["4. close"])
        volume = int(day["5. volume"])

        SQL_INSERT = f"""
        INSERT INTO prices_from_agm (date, Symbol, open, high, low, close, volume)
        VALUES ('{date}', '{config.SYMBOL_GOOG}', {open_}, {high}, {low}, {close}, {volume})
        """
        result = config.engine.execute(SQL_INSERT)
        result.close()


def _data_msft():
    end_point = f"{config.end_point_msft_pop}"
    print(f"Getting data from Miscrosoft {end_point}...")
    r = requests.get(end_point)
    data_msft = r.json()

    with open(f"/tmp/{config.SYMBOL_MSFT}.json", "w") as f:
        json.dump(data_msft, f)


def _insert_msft():
    with open(f"/tmp/{config.SYMBOL_MSFT}.json", "r") as f:
        data_msft = json.load(f)

    for date_str, day in data_msft["Time Series (Daily)"].items():
        date = datetime.strptime(date_str, "%Y-%m-%d")
        open_ = float(day["1. open"])
        high = float(day["2. high"])
        low = float(day["3. low"])
        close = float(day["4. close"])
        volume = int(day["5. volume"])

        SQL_INSERT = f"""
        INSERT INTO prices_from_agm (date, Symbol, open, high, low, close, volume)
        VALUES ('{date}', '{config.SYMBOL_MSFT}', {open_}, {high}, {low}, {close}, {volume})
        """
        result = config.engine.execute(SQL_INSERT)
        result.close()


if __name__ == "__main__":
    _data_amzn()
    _data_goog()
    _data_msft()
    _insert_amzn()
    _insert_goog()
    _insert_msft()
