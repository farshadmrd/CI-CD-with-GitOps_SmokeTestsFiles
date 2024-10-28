import requests
import logging
import pytest
import time

# Set up logging
logging.basicConfig(level=logging.INFO)

# Default base URL
BASE_URL = "http://127.0.0.1:8080"
MAX_RETRIES = 10
RETRY_DELAY = 2  # seconds

# Test API Gateway response
def test_api_gateway_response():
    gateway_url = f"{BASE_URL}/hello"
    logging.info(f"Testing API Gateway response at {gateway_url}...")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(gateway_url, timeout=5)
            if response.status_code == 200:
                assert response.text == 'Hello from Config Server!', f"Unexpected response from API Gateway! Got: {response.text}"
                logging.info("API Gateway responded successfully with status 200.")
                break  # Exit the loop if the response is successful
            elif response.status_code == 503:
                logging.warning(f"Attempt {attempt} received 503 Service Unavailable. Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                pytest.fail(f"Unexpected status code: Expected 200 but got {response.status_code}")
                break
        except requests.exceptions.ConnectionError:
            logging.warning(f"Attempt {attempt} failed: Connection error. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
    else:
        pytest.fail(f"API Gateway did not respond with status 200 after {MAX_RETRIES} attempts.")
