class TestPagesAccess:

    def test_competitions_page_without_being_logged_should_fail(self, client):
        # Trying to reach it should redirect
        response = client.get('/competitions')
        assert response.status_code == 302
        # Following redirection should bring to registration page
        response = client.get('/competitions', follow_redirects=True)
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
    
    def test_book_without_being_logged_should_fail(self, client, monkeypatch):


        response = client.get('/book/competition_test1/club_test1', follow_redirects=True)

        assert response.status_code == 200
        data = response.data.decode()
        print(data)
        assert "Welcome to the GUDLFT Registration Portal!" in data