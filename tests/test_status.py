# from fastapi import status, HTTPException
from fastapi.testclient import TestClient
from main import app

# from core.config import settings


def test_main_page():
    client = TestClient(app)
    result = client.get("/")
    assert result.status_code == 200
