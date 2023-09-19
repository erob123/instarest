from collections.abc import Generator
from unittest.mock import create_autospec
import pytest
from examples.example_app import app
from instarest.routers.rest import get_db


@pytest.fixture(scope="function", autouse=True)
def setup_teardown_function(db) -> Generator:
    def mock_db():
        yield create_autospec(db)

    app.dependency_overrides = {get_db: mock_db}
    yield
    app.dependency_overrides = {}
