"""Never call the real API in a test. FakeSession pretends to be requests.Session."""
from insurecraft_etl import extract  # noqa: F401


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self._payload


class FakeSession:
    def __init__(self):
        self.calls = []

    def post(self, url, json, timeout):
        self.calls.append(json["postcodes"])
        result = [{"query": pc, "result": {"region": "East of England", "country": "England",
                                           "admin_district": "Norwich", "latitude": 52.6, "longitude": 1.3}}
                  for pc in json["postcodes"]]
        return FakeResponse({"status": 200, "result": result})


# TODO: test that lookup_postcodes sends 250 postcodes in three calls (100, 100, 50).
# TODO: test that a postcode the API cannot find is kept with empty columns.
