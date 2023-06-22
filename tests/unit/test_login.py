class TestLoginClass:

    def test_index(self, client):
        response = client.get("/")
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome to the GUDLFT" in data
    
    def test_login_existing_mail_should_success(self, client, monkeypatch):
        response = client.post("/login", data={"email": "admin@irontemple.com"}, follow_redirects=True)
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome, admin@irontemple.com" in data
    
    def test_login_bad_email_sould_fail(self, client):
        response = client.post("/login", data={"email": "bad@email.com"}, follow_redirects=True)
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome to the GUDLFT" in data
        assert "No account exists with this mail : &#39;bad@email.com&#39;" in data
    
    def test_login_no_email_should_fail(self, client):
        response = client.post("/login", data={"email": ""}, follow_redirects=True)
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome to the GUDLFT" in data
        assert "No account exists with this mail : &#39;&#39;" in data
