import pytest
import requests
import logging

# Fixture for the base URL
@pytest.fixture
def base_url():
    return 'http://localhost'

# Set up logging
logging.basicConfig(level=logging.INFO)

# Test services health
@pytest.mark.parametrize("service_name, port", [
    ("Config Server", 8888),
    ("Eureka Server", 8761),
    ("Hello World", 8081),
    ("API Gateway", 8080),
])
def test_service_health(base_url, service_name, port):
    url = f"{base_url}:{port}/actuator/health"
    logging.info(f"Checking health for {service_name} at {url}...")
    
    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 200, f"Health check failed for {service_name}! Expected 200, got {response.status_code}"
        assert 'UP' in response.json()['status'], f"{service_name} is not UP!"
    except requests.exceptions.ConnectionError:
        pytest.fail(f"Failed to connect to {service_name} at {url}. Connection error.")

# Test Hello World service response
def test_hello_world_response(base_url):
    hello_world_url = f"{base_url}:8081/hello"
    logging.info(f"Testing Hello World service response at {hello_world_url}...")
    
    try:
        response = requests.get(hello_world_url, timeout=5)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code} from Hello World!"
        assert response.text == 'Hello from Config Server!', f"Unexpected response from Hello World! Got: {response.text}"
    except requests.exceptions.ConnectionError:
        pytest.fail(f"Failed to connect to Hello World service at {hello_world_url}. Connection error.")

# Test API Gateway response
def test_api_gateway_response(base_url):
    gateway_url = f"{base_url}:8080/hello"
    logging.info(f"Testing API Gateway response at {gateway_url}...")
    
    try:
        response = requests.get(gateway_url, timeout=5)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code} from API Gateway!"
        assert response.text == 'Hello from Config Server!', f"Unexpected response from API Gateway! Got: {response.text}"
    except requests.exceptions.ConnectionError:
        pytest.fail(f"Failed to connect to API Gateway at {gateway_url}. Connection error.")
