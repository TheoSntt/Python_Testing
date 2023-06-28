from utilities.booking_helper import Booking_Helper
from tests.json_mock import mock_load_json


class TestHelperFunctions:

    helper = Booking_Helper()

    def test_maximum_places_allowed(self):
        clubs = mock_load_json("clubs")
        competitions = mock_load_json("competitions")

        _MAX_PLACE = 12
        """
        CLUB 1 Points : 30
        CLUB 2 Points : 8
        CLUB 3 Points : 0
        _______

        COMP 1 Places : 50 (6 booked by club 1, 6 booked by club 2)
        COMP 2 Places : 15
        COMP 3 Places : 6
        """
        assert self.helper.max_places_allowed(competitions[0], clubs[0], _MAX_PLACE) == 6
        assert self.helper.max_places_allowed(competitions[1], clubs[0], _MAX_PLACE) == 12
        assert self.helper.max_places_allowed(competitions[1], clubs[1], _MAX_PLACE) == 8
        assert self.helper.max_places_allowed(competitions[2], clubs[0], _MAX_PLACE) == 6
        assert self.helper.max_places_allowed(competitions[2], clubs[2], _MAX_PLACE) == 0
        assert self.helper.max_places_allowed(competitions[2], clubs[1], _MAX_PLACE) == 6
        assert self.helper.max_places_allowed(competitions[3], clubs[0], _MAX_PLACE) == 12