import sqlalchemy.exc
import psycopg2
from sqlalchemy import create_engine

BASE_URL = "https://www.alphavantage.co/query"
API_KEY_POPULATOR = "OYSVHCU8LGQYED75"
API_KEY_DAGS = "MM617540JHWT3078"
API_KEY_TESTS_AMZN = "IC4WEDMBRMKTEWYD"
API_KEY_TESTS_GOOG = "APJ1AX2E8WY1QZZA"
API_KEY_TESTS_MSFT = "S4C1I5VGD0PFASCX"
API_KEY_TESTS_AMZN2 = "LDH7V295X6FEYF2F"
API_KEY_TESTS_GOOG2 = "6UMCFJ90B8PBOLB4"
API_KEY_TESTS_MSFT2 = "RG88NF7LEP3YLY4E"


SYMBOL_AMZN = "AMZN"
SYMBOL_GOOG = "GOOG"
SYMBOL_MSFT = "MSFT"

# API_KEY for populatorDB.py

end_point_amzn_pop = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_AMZN}"
    f"&apikey={API_KEY_POPULATOR}&datatype=json"
)

end_point_goog_pop = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_GOOG}"
    f"&apikey={API_KEY_POPULATOR}&datatype=json"
)

end_point_msft_pop = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_MSFT}"
    f"&apikey={API_KEY_POPULATOR}&datatype=json"
)

# API_KEY for tests

end_point_amzn_test = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_AMZN}"
    f"&apikey={API_KEY_TESTS_AMZN}&datatype=json"
)

end_point_goog_test = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_GOOG}"
    f"&apikey={API_KEY_TESTS_GOOG}&datatype=json"
)

end_point_msft_test = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_MSFT}"
    f"&apikey={API_KEY_TESTS_MSFT}&datatype=json"
)

# API_KEY 2 for tests

end_point_amzn_test2 = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_AMZN}"
    f"&apikey={API_KEY_TESTS_AMZN2}&datatype=json"
)

end_point_goog_test2 = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_GOOG}"
    f"&apikey={API_KEY_TESTS_GOOG2}&datatype=json"
)

end_point_msft_test2 = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_MSFT}"
    f"&apikey={API_KEY_TESTS_MSFT2}&datatype=json"
)

# API_KEY for Dags

end_point_amzn_dag = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_AMZN}"
    f"&apikey={API_KEY_DAGS}&datatype=json"
)

end_point_goog_dag = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_GOOG}"
    f"&apikey={API_KEY_DAGS}&datatype=json"
)

end_point_msft_dag = (
    f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={SYMBOL_MSFT}"
    f"&apikey={API_KEY_DAGS}&datatype=json"
)

DB_USER = "postgres"
DB_PASS = "postgres"
IP = "db_postgres"
DB_PORT = "5432"
DB_NAME = "prices_from_agm"
DB_NAME_BASE = "postgres"
conn_db = "postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME_BASE}"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME}")
engine2 = create_engine(
    f"postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME_BASE}"
)

conn_dic = {
    "DB_USER": "postgres",
    "DB_PASS": "postgres",
    "IP": "db_postgres",
    "DB_PORT": "5432",
    "DB_NAME": "prices_from_agm",
    "DB_NAME_BASE": "postgres",
}

if __name__ == "__main__":
    ()
