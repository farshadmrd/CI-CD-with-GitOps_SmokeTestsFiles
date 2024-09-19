import requests

def test_config_server():
    """Smoke test for Config Server"""
    response = requests.get('http://localhost:8888/actuator/health')
    assert response.status_code == 200
    assert 'UP' in response.json()['status']

def test_eureka_server():
    """Smoke test for Eureka Server"""
    response = requests.get('http://localhost:8761/actuator/health')
    assert response.status_code == 200
    assert 'UP' in response.json()['status']

def test_hello_world():
    """Smoke test for Hello World service"""
    response = requests.get('http://localhost:8081/actuator/health')
    assert response.status_code == 200
    assert 'UP' in response.json()['status']
    # Test hello-world response
    hello_response = requests.get('http://localhost:8081/hello')
    assert hello_response.status_code == 200
    assert hello_response.text == 'Hello from Config Server!'

def test_api_gateway():
    """Smoke test for API Gateway"""
    response = requests.get('http://localhost:8080/actuator/health')
    assert response.status_code == 200
    assert 'UP' in response.json()['status']
    # Test routed response through API Gateway
    gateway_response = requests.get('http://localhost:8080/hello')
    assert gateway_response.status_code == 200
    assert gateway_response.text == 'Hello fom Config Server!'
