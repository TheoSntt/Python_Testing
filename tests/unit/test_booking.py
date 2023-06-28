from tests.json_mock import mock_load_json


class TestBookingClass:
    """
    STARTING POINT :

    CLUB 1 Points : 30
    CLUB 2 Points : 8
    CLUB 3 Points : 0
    _______

    COMP 1 Places : 50 (6 booked by club 1, 6 booked by club 2)
    COMP 2 Places : 15
    COMP 3 Places : 6
    """
    def test_booking_less_places_than_available_points_should_success(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 4})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Great-booking complete!" in data
    """
    CLUB 1 Points : 26
    CLUB 2 Points : 8
    CLUB 3 Points : 0
    _______

    COMP 1 Places : 46 (10 booked by club 1, 6 booked by club 2)
    COMP 2 Places : 15
    COMP 3 Places : 6
    """
    def test_booking_more_places_than_available_points_should_fail(self, client):
        # Testing with club 3
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test3",
                                                        "places": 10})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 0 places" in data
        # Testing with club 2 who has 8 points
        response = client.post("/purchasePlaces", data={"competition": "competition_test2",
                                                        "club": "club_test2",
                                                        "places": 9})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 8 places" in data
    """
    CLUB 1 Points : 26
    CLUB 2 Points : 8
    CLUB 3 Points : 0
    _______

    COMP 1 Places : 46 (10 booked by club 1, 6 booked by club 2)
    COMP 2 Places : 15
    COMP 3 Places : 6
    """
    def test_booking_more_than_12_places_should_fail(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test2",
                                                        "club": "club_test1",
                                                        "places": 15})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 12 places" in data
    
    def test_booking_more_than_12_places_in_two_iterations_should_fail(self, client):
        # Now trying to buy 12 places twice with club 1. First one should work
        response = client.post("/purchasePlaces", data={"competition": "competition_test2",
                                                        "club": "club_test1",
                                                        "places": 10})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Great-booking complete!" in data
        # Second iteration should fail
        response = client.post("/purchasePlaces", data={"competition": "competition_test2",
                                                        "club": "club_test1",
                                                        "places": 5})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 2 places" in data

    """
    CLUB 1 Points : 16
    CLUB 2 Points : 5
    CLUB 3 Points : 0
    _______

    COMP 1 Places : 46 (10 booked by club 1, 6 booked by club 2)
    COMP 2 Places : 5 (10 booked by club 1)
    COMP 3 Places : 6
    """   
    def test_booking_max_allowed_places_respected_in_ui(self, client):
        # Competition : 46 places / Club : 16 points / Already booked : 10
        response = client.get('/book/competition_test1/club_test1')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="6"' in data

        # Competition : 5 places / Club : 5 points / Already booked : 0
        response = client.get('/book/competition_test2/club_test2')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="8"' in data

        # Competition : 6 places / Club : 46 points
        response = client.get('/book/competition_test3/club_test1')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="6"' in data

    def test_booking_in_past_competition_should_fail(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test4",
                                                        "club": "club_test1",
                                                        "places": 1})
        assert response.status_code == 200
        data = response.data.decode()
        assert "The competition is closed" in data