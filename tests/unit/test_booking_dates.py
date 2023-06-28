class TestBookingDatesClass:
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
    def test_booking_a_future_competition_should_sucess(self, client, monkeypatch):
        response = client.post("/purchasePlaces", data={"competition": "competition_test3",
                                                        "club": "club_test1",
                                                        "places": 1})
        assert response.status_code == 200
        data = response.data.decode()
        print(data)
        assert "Welcome, test1@email.fr" in data
        assert "Points available: 29" in data
        assert "Number of Places: 5" in data
        assert "Great-booking complete" in data

    def test_booking_in_past_competition_should_fail(self, client):
        response = client.post("/purchasePlaces", data={"competition": "competition_test4",
                                                        "club": "club_test1",
                                                        "places": 1})
        assert response.status_code == 200
        data = response.data.decode()
        assert "The competition is closed" in data