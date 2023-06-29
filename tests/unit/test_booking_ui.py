from tests.json_mock import mock_load_json


class TestBookingUIClass:
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
    def test_booking_max_allowed_places_respected_in_ui(self, client):
        clubs = mock_load_json("clubs")
        
        # Logging as club 1
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Competition : 50 places / Club : 30 points / Already booked : 6
        response = client.get('/book/competition_test1')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="6"' in data
        
        # Logging as club 2
        with client.session_transaction() as session:
            session["logged_club"] = clubs[1]
        # Competition : 15 places / Club : 8 points / Already booked : 0
        response = client.get('/book/competition_test2')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="8"' in data
        
        # Logging as club 1
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Competition : 6 places / Club : 50 points
        response = client.get('/book/competition_test3')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="6"' in data

    def test_booking_link_not_diplayed_when_no_points_left(self, client):

        clubs = mock_load_json("clubs")
        
        # Test with first club, who has lots of points
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Should have the booking link for all future competitions, exept the fifth, which is full
        response = client.get("/competitions")
        assert response.status_code == 200
        data = response.data.decode()
        assert '<a href="/book/competition_test1">Book Places</a>' in data
        assert '<a href="/book/competition_test2">Book Places</a>' in data
        assert '<a href="/book/competition_test3">Book Places</a>' in data
        assert '<a href="/book/competition_test5">Book Places</a>' not in data
        
        # Test with third club, who has no points
        with client.session_transaction() as session:
            session["logged_club"] = clubs[2]
        # Should have no links
        response = client.get("/competitions")
        assert response.status_code == 200
        data = response.data.decode()
        assert '<a href="/book/competition_test1">Book Places</a>' not in data
        assert '<a href="/book/competition_test2">Book Places</a>' not in data
        assert '<a href="/book/competition_test3">Book Places</a>' not in data
        assert '<a href="/book/competition_test5">Book Places</a>' not in data

        # Test with second club, who has points, but has already booked 12 places in third comp
        with client.session_transaction() as session:
            session["logged_club"] = clubs[1]
        # Should have the booking link for all future competitions, except third and fifth
        response = client.get("/competitions")
        assert response.status_code == 200
        data = response.data.decode()
        assert '<a href="/book/competition_test1">Book Places</a>' in data
        assert '<a href="/book/competition_test2">Book Places</a>' in data
        assert '<a href="/book/competition_test3">Book Places</a>' not in data
        assert '<a href="/book/competition_test5">Book Places</a>' not in data


    def test_booking_link_not_diplayed_for_past_competition(self, client):

        clubs = mock_load_json("clubs")
        
        # Test with first club
        with client.session_transaction() as session:
            session["logged_club"] = clubs[0]
        # Should have the booking link for all future competitions but not the past one
        response = client.get("/competitions")
        assert response.status_code == 200
        data = response.data.decode()
        assert '<a href="/book/competition_test1">Book Places</a>' in data
        assert '<a href="/book/competition_test2">Book Places</a>' in data
        assert '<a href="/book/competition_test3">Book Places</a>' in data
        assert '<a href="/book/competition_test4">Book Places</a>' not in data
       
        # Test with second club
        with client.session_transaction() as session:
            session["logged_club"] = clubs[1]
        # Should have the booking link for all future competitions (execpt third) but not the past one
        response = client.get("/competitions")
        assert response.status_code == 200
        data = response.data.decode()
        assert '<a href="/book/competition_test1">Book Places</a>' in data
        assert '<a href="/book/competition_test2">Book Places</a>' in data
        assert '<a href="/book/competition_test4">Book Places</a>' not in data