import pytest

from ..app import *

def test_index_route():

    response = index().get("/")

    assert response.status_code == 200
    # assert response.data.decode('utf-8') == ""
