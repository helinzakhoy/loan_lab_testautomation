import pytest
from src.client.api_client import APIClient

@pytest.fixture
def api():
    return APIClient("https://souderbroder-loan-lab.lovable.app")
