import dags.dummy_dag as dummy
import dags.configinc as config
import psycopg2


def test_aggregation_avg_amzn():
    SQL_QUERY_AMZN = """
    SELECT AVG(close) FROM prices_from_agm WHERE extract('ISODOW' FROM date) < 6 
        and date >= CURRENT_DATE - 9 AND symbol = 'AMZN'
    """
    conn = config.engine.execute
    conn(SQL_QUERY_AMZN)


def test_aggregation_avg_goog():
    SQL_QUERY_GOOG = """
    SELECT AVG(close) FROM prices_from_agm WHERE extract('ISODOW' FROM date) < 6 
        and date >= CURRENT_DATE - 9 AND symbol = 'GOOG'
    """
    conn = config.engine.execute
    conn(SQL_QUERY_GOOG)


def test_aggregation_avg_msft():
    SQL_QUERY_MSFT = """
    SELECT AVG(close) FROM prices_from_agm WHERE extract('ISODOW' FROM date) < 6 
        and date >= CURRENT_DATE - 9 AND symbol = 'MSFT'
    """
    conn = config.engine.execute
    conn(SQL_QUERY_MSFT)
