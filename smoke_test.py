import requests
import logging
import pytest

# Set up logging
logging.basicConfig(level=logging.INFO)

# Default base URL
BASE_URL = "http://127.0.0.1:8080"

# Test API Gateway response
def test_api_gateway_response():
    gateway_url = f"{BASE_URL}/hello"
    logging.info(f"Testing API Gateway response at {gateway_url}...")
    
    try:
        response = requests.get(gateway_url, timeout=5)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code} from API Gateway!"
        assert response.text == 'Hello from Config Server!', f"Unexpected response from API Gateway! Got: {response.text}"
    except requests.exceptions.ConnectionError:
        pytest.fail(f"Failed to connect to API Gateway at {gateway_url}. Connection error.")
