from datetime import datetime
from pathlib import Path
import json
from time import sleep
import requests  # type: ignore
import sqlalchemy.exc
import psycopg2
from sqlalchemy import create_engine
from datetime import date
import configinc as config

# create main table


def _sql_create_table():
    SQL_CREATE = """
    CREATE TABLE IF NOT EXISTS prices_from_agm (id BIGSERIAL PRIMARY KEY,
        date date NOT NULL,
        Symbol text,
        open float,
        high float,
        low float,
        close float,
        volume float)
    """
    result = config.engine.execute(SQL_CREATE)
    result.close()


if __name__ == "__main__":
    _sql_create_table()
