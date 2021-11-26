import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine import result
import dags.configinc as config


def test_sql_conn_db():
    ok = config.engine == 200
    return ok


def test_sql_create_operate_table():
    SQL_CREATE = """
    CREATE TABLE IF NOT EXISTS test (id BIGSERIAL PRIMARY KEY,
        date date NOT NULL,
        some_text text)
    """
    SQL_INSERT_DATA = """
    INSERT INTO test (date, some_text) VALUES ('1970-01-01', 'test-test')
    """
    SQL_QUERY_DATA = """
    SELECT * FROM test
    """
    SQL_DROP_TABLE = """
    DROP TABLE test
    """
    conn = config.engine2.execute
    conn(SQL_CREATE)
    conn(SQL_INSERT_DATA)
    conn(SQL_QUERY_DATA)
    conn(SQL_DROP_TABLE)
