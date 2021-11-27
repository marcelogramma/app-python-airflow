import dags.configinc as config
import requests
import datetime

# Test for Amazon API


def test_api_status_content_amzn():
    headers = {
        "Accept": "*/*",
        "User-Agent": "request",
    }
    url = f"{config.end_point_amzn_test}"
    respuesta = requests.get(url, headers=headers)
    assert respuesta.status_code == 200
    assert respuesta.content != None
    assert respuesta.json()["Meta Data"]["2. Symbol"] == "AMZN"
    assert respuesta.json()["Meta Data"][
        "3. Last Refreshed"
    ] <= datetime.datetime.now().strftime("%Y-%m-%d")


# Test for Google API


def test_api_content_goog():
    url = f"{config.end_point_goog_test2}"
    respuesta = requests.get(url)
    assert respuesta.content != None
    assert respuesta.json()["Meta Data"]["2. Symbol"] == "GOOG"
    assert respuesta.json()["Meta Data"][
        "3. Last Refreshed"
    ] <= datetime.datetime.now().strftime("%Y-%m-%d")


# Test for Microsoft API

# def test_api_content_msft():
#     url = f"{config.end_point_msft_test}"
#     respuesta = requests.get(url)
#     assert respuesta.content != None
#     assert respuesta.json()["Meta Data"]["2. Symbol"] == "MSFT"
#     assert respuesta.json()["Meta Data"]["3. Last Refreshed"] < datetime.datetime.now().strftime("%Y-%m-%d")
