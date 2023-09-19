from uuid import uuid4
from unittest.mock import patch
from fastapi.testclient import TestClient
from examples.example_app import EmptyTestModel


@patch("examples.example_app.test_router.crud_base", autospec=True)
def test_read_valid_id(mock_crud, client: TestClient):
    # setup the request body
    id = uuid4()

    # mock the db call
    mock_crud.get.return_value = EmptyTestModel(id=id, bool_field=False, title="test")

    # make the request
    response = client.get(
        f"/test/{id}/",
        headers={},
    )

    # check that the mock was called with the correct method
    mock_crud.get.assert_called_once()

    assert response.status_code == 200
    assert response.json()["id"] == str(id)


@patch("examples.example_app.test_router.crud_base", autospec=True)
def test_read_invalid_id(mock_crud, client: TestClient):
    # setup the request body
    id = uuid4()

    # mock the db call
    mock_crud.get.return_value = None

    # make the request
    response = client.get(
        f"/test/{id}/",
        headers={},
    )

    # check that the mock was called with the correct method
    mock_crud.get.assert_called_once()

    assert response.status_code == 400
    assert response.json()["detail"] == f"EmptyTest with id: {id} not found"
