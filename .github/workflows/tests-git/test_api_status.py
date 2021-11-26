import requests

# Test for API


def test_api_status_content():
    headers = {
        "Accept": "*/*",
        "User-Agent": "request",
    }
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOG&interval=5min&apikey=SENYX5F24YYKJKJS"
    respuesta = requests.get(url, headers=headers)
    assert respuesta.status_code == 200
    assert respuesta.content != None
