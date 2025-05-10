from fastapi.testclient import TestClient
import pytest

import parametrize_from_file


def test_if_root_endpoint_is_up(test_client: TestClient):
    response = test_client.get("/")
    assert response.status_code == 200



#FIXME: this has to be moved or deleted
# @parametrize_from_file
# @pytest.mark.usefixtures("db_setup_teardown")
# def test_insert_part(test_client: TestClient, test_part):
#     response = test_client.post("/check_db", json=test_part)
#     assert response.status_code == 200
#
