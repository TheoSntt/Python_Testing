class TestBookingClass:

    
    def test_booking_less_places_than_available_points_should_success(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test2",
                                                        "places": 6})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Great-booking complete!" in data

    def test_booking_more_places_than_available_points_should_fail(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test2",
                                                        "places": 10})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 8 places" in data
    
    def test_booking_more_than_12_places_should_fail(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 15})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 12 places" in data
    
    def test_booking_more_than_12_places_in_two_iterations_should_fail(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 12})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Great-booking complete!" in data
        # Second iteration
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 12})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 12 places" in data

    
    def test_booking_max_allowed_places_respected_in_ui(self, client):

        # with client.session_transaction() as session:
        #     session["logged_club"] = {'name': 'club_test1'}

        # Competition : 50 places / Club : 20 points
        response = client.get('/book/competition_test1/club_test1')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="12"' in data

        # Competition : 15 places / Club : 20 points
        response = client.get('/book/competition_test2/club_test1')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="12"' in data

        # Competition : 6 places / Club : 20 points
        response = client.get('/book/competition_test3/club_test1')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="6"' in data
