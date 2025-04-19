import requests

def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    
    # Fake user data we are sending
    new_user = {
        "name": "Alt Bozon",
        "email": "altbozon@example.com",
        "username": "altbozon"
    }
    
    # Send a POST request
    response = requests.post(url, json=new_user)
    
    # Assert that the response is successful (should be 201 Created)
    assert response.status_code == 201

    # Get the JSON response
    data = response.json()

    # Assert that the server returned the data we sent
    assert data["name"] == new_user["name"]
    assert data["email"] == new_user["email"]
    assert data["username"] == new_user["username"]
