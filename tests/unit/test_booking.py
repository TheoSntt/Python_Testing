class TestBookingClass:

    
    def test_booking_less_places_than_available_points_should_success(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Competition Test 1",
                                                        "club": "Club Test 2",
                                                        "places": 6})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Great-booking complete!" in data

    def test_booking_more_places_than_available_points_should_fail(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Competition Test 1",
                                                        "club": "Club Test 2",
                                                        "places": 10})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 8 places" in data