import requests

def test_api_availability(url="http://localhost:8081/hello"):
    response = requests.get(url)
    expected_response = "Hello"
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.text == expected_response, f"Expected response body '{expected_response}', got {response.text}"

if __name__ == "__main__":
    print("Running tests")

    try:
        test_api_availability()
    except AssertionError as e:
        # print(f"Test failed: {e}")
        print("Test failed")

    else:  
        print("All tests ran successfully!")
