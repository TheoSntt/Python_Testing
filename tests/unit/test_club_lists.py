class TestClubs:

    def test_clubs_url(self, client):
        response = client.get("/showClubs")
        assert response.status_code == 200
        data = response.data.decode()
        assert "List of clubs || GUDLFT" in data