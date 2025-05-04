import pytest
from fastapi.testclient import TestClient

from fastapi_curso.app import app


@pytest.fixture
def client():
    return TestClient(app)
