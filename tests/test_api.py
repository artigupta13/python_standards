from service.users import fetch_user


def test_fetch_users(requests_mock):
    user_id = 1
    expected_data = {
        "id": user_id,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        },
    }

    requests_mock.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}", json=expected_data
    )

    result = fetch_user(user_id)

    assert result == expected_data
