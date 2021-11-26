import dags.dummy_dag as dummy
from os import remove
from os import path


def test_query_for_plots():
    df_amzn = dummy._query_for_plots()
    df_goog = dummy._query_for_plots()
    df_msft = dummy._query_for_plots()
    assert dummy._query_for_plots() == df_amzn
    assert dummy._query_for_plots() == df_goog
    assert dummy._query_for_plots() == df_msft
    if path.exists("/opt/airflow/data/plots/"):
        remove("/opt/airflow/data/plots/close.png")
        remove("/opt/airflow/data/plots/open.png")
        remove("/opt/airflow/data/plots/volume.png")
