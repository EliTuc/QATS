import pytest
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
regres_url = "https://reqres.in/"


def get_users(page_number):
    try:
        response = requests.get(regres_url + 'api/users?page=' + str(page_number), verify=False)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        pytest.fail(f"Failed to retrieve users due to: {str(e)}")


def test_get_users_page_2():
    json_response = get_users(2)

    # Assert that we received a 200 OK response
    assert json_response, "No response received from the server"

    # Check "total"
    total = json_response.get('total', 0)
    assert total, "Total count is missing or zero"

    # Check "last_name" for the first and second user in "data"
    data = json_response.get('data', [])
    assert len(data) > 1, "Insufficient data received"
    assert "last_name" in data[0], "First user is missing the 'last_name' key"
    assert "last_name" in data[1], "Second user is missing the 'last_name' key"

    # Count number of received users in “data” and compare it to the received value
    last_user_id = data[-1].get("id", 0)
    assert total == last_user_id, f"Expected total {total} but got {last_user_id}"