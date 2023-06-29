class TestIntegrationClass:

    def test_full_userpath_login_bookings_logout(self, client):
        # Loging as first club
        response = client.post("/login", data={"email": "test1@email.fr"}, follow_redirects=True)
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome, test1@email.fr" in data

        # Checking redirection to the competitions
        assert "Competitions || GUDLFT" in data

        # UI AND DATA CHECK
        # Checking (with the first competition) if the information is correctly displayed
        assert "competition_test1" in data
        assert "Date: 2025-06-22 08:00:00" in data
        assert '<a href="/book/competition_test1">Book Places</a>' in data
        # Checking (with the fifth competition) if the UI limitation on booking works
        assert "competition_test5" in data
        assert "Date: 2028-11-05 09:00:00" in data
        # (Comp 5 has no places left)
        assert '<a href="/book/competition_test5">Book Places</a>' not in data
        # Checking (with the fourth competition) if the UI limitation on booking works
        assert "competition_test4" in data
        assert "Date: 2020-11-05 09:00:00" in data
        # (Comp 4 is past)
        assert '<a href="/book/competition_test4">Book Places</a>' not in data

        # Checking UI limitations on a given booking page
        response = client.get('/book/competition_test1')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="6"' in data
        
        # START THE BOOKING PROCESS

        # BOOKING 4 PLACES TO COMP 1 SHOULD WORK
        # Competition 1 : 50 places | Club 1 : 30 points | Booked : 6
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 4})
        data = response.data.decode()
        assert "Great-booking complete" in data

        assert "Points available: 26" in data
        assert "Number of Places: 46" in data
        assert "Already booked by your club: 10" in data
        assert '<a href="/book/competition_test1">Book Places</a>' in data

        # New UI limitations
        response = client.get('/book/competition_test1')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="2"' in data

        # BOOKING 4 MORE PLACES TO COMP 1 SHOULD FAIL
        # Competition 1 : 46 places | Club 1 : 26 points | Booked : 10
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 4})
        data = response.data.decode()
        assert "You can only book a maximum of 2 places" in data

        # Points balance should not change
        assert "Points available: 26" in data
        assert "Number of Places: 46" in data
        assert "Already booked by your club: 10" in data
        assert '<a href="/book/competition_test1">Book Places</a>' in data

        #  UI limitations should not change
        response = client.get('/book/competition_test1')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="2"' in data

        # BOOKING 2 MORE PLACES TO COMP 1 SHOULD SUCCESS
        # Competition 1 : 46 places | Club 1 : 26 points | Booked : 10
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 2})
        data = response.data.decode()

        assert "Great-booking complete" in data
        # New points balance
        assert "Points available: 24" in data
        assert "Number of Places: 44" in data
        assert "Already booked by your club: 12" in data
        # Booking link should be hidden
        assert '<a href="/book/competition_test1">Book Places</a>' not in data

        # # New UI limitations
        response = client.get('/book/competition_test1')
        data = response.data.decode()
        assert 'name="places" value="1" min="1" max="0"' in data

        # BOOKING 1 MORE PLACE TO COMP 1 SHOULD FAIL
        # Competition 1 : 44 places | Club 1 : 24 points | Booked : 12
        response = client.post("/purchasePlaces", data={"competition": "competition_test1",
                                                        "club": "club_test1",
                                                        "places": 1})
        data = response.data.decode()

        assert "You can only book a maximum of 0 places" in data

        # Unchanged points balance
        assert "Points available: 24" in data
        assert "Number of Places: 44" in data
        assert "Already booked by your club: 12" in data
        # Booking link should still be hidden
        assert '<a href="/book/competition_test1">Book Places</a>' not in data

        # LOGOUT ---------------------------------------------------------------------------------------------
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome to the GUDLFT" in data

        # TRY TO REACH COMP PAGES TO SEE IF LOGOUT IS EFFECTIVE
        response = client.get('/competitions')
        assert response.status_code == 302
        response = client.get('/competitions', follow_redirects=True)
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome to the GUDLFT" in data

        # TRY TO REACH CLUBS PAGES SHOULD SUCCESS
        response = client.get('/clubs')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'club_test1' in data
        assert 'club_test2' in data
        assert 'club_test3' in data