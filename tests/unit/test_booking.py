from tests.json_mock import mock_load_json


class TestBookingClass:
    """
    DATA :

    CLUB 1 Points : 30
    CLUB 2 Points : 8
    CLUB 3 Points : 0
    _______

    COMP 1 Places : 50 (6 booked by club 1, 6 booked by club 2)
    COMP 2 Places : 15
    COMP 3 Places : 6
    """
    def test_booking_less_places_than_available_points_should_success(self, client):
        # Logging as club 1
        clubs = mock_load_json("clubs")
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Booking the places
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 4})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Great-booking complete!" in data

    def test_booking_more_places_than_available_points_should_fail(self, client):
        # Logging as club 1
        clubs = mock_load_json("clubs")
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Booking the places
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

    def test_booking_more_than_12_places_should_fail(self, client):
        # Logging as club 1
        clubs = mock_load_json("clubs")
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Booking the places
        response = client.post("/purchasePlaces", data={"competition": "competition_test2",
                                                        "club": "club_test1",
                                                        "places": 15})
        assert response.status_code == 200
        data = response.data.decode()
        assert "You can only book a maximum of 12 places" in data
    
    def test_booking_more_than_12_places_in_two_iterations_should_fail(self, client):
        # Logging as club 1
        clubs = mock_load_json("clubs")
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Booking the places
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
