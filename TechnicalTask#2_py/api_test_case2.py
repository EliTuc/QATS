import pytest
import requests

# Base URL for the API 
regres_url = "https://reqres.in"

# Endpoint for the users
ENDPOINT = "/api/users"

# Time limit for response
TIME_LIMIT = 0.2

# Sample data to POST
user_data = {"name": "morpheus", "job": "leader"}

def test_post_create_user():
    url = regres_url + ENDPOINT

    # Send POST request
    response = requests.post(url, json=user_data, verify=False)

    # Assertions
    # Check HTTP status code
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}. Response content: {response.content}"

    # Check ID exists in the response
    assert "id" in response.json(), f"Expected 'id' in response, but got {response.json()}"

    # Check created date exists in the response
    assert "createdAt" in response.json(), f"Expected 'createdAt' in response, but got {response.json()}"

    # Check response time
    actual_response_time = response.elapsed.total_seconds()
    assert actual_response_time < TIME_LIMIT, f"Expected response time < {TIME_LIMIT} seconds, but got {actual_response_time} seconds"

if __name__ == "__main__":
    pytest.main()
