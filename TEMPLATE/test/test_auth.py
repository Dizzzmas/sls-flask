from TEMPLATE.db.fixtures import DEFAULT_PASSWORD


def test_login(client_unauthenticated, user, db_session):
    response = client_unauthenticated.post(
        "/api/auth/login", json=dict(email=user.email, password=DEFAULT_PASSWORD)
    )
    assert response.status_code == 200
    assert response.json.get("access_token") is not None
    assert response.json.get("refresh_token") is not None