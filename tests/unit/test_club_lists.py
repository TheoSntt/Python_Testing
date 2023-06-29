class TestClubs:

    def test_clubs_url(self, client):
        response = client.get("/clubs")
        assert response.status_code == 200
        data = response.data.decode()
        assert "List of clubs || GUDLFT" in data
    
    def test_list_display(self, client):
        response = client.get('/clubs')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'club_test1' in data
        assert 'test1@email.fr' in data
        assert 'Points: 30' in data

        assert 'club_test2' in data
        assert 'test2@email.fr' in data
        assert 'Points: 8' in data

        assert 'club_test2' in data
        assert 'test3@email.fr' in data
        assert 'Points: 0' in data