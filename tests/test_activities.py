from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_count = len(activities)

    # Act
    response = client.get("/activities")
    response_data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(response_data) == expected_activity_count
    assert "Chess Club" in response_data
    assert response_data["Chess Club"]["participants"] == activities["Chess Club"]["participants"]