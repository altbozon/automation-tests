import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # Basic checks
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10

    # Check first user's fields
    user = data[0]
    assert "name" in user
    assert "email" in user
    assert "id" in user

    # New: Check specific expected value
    expected_name = "Leanne Graham"
    assert user["name"] == expected_name, f"Expected name '{expected_name}' but got '{user['name']}'"
