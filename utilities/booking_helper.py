from datetime import datetime

class Booking_Helper:
    """Utility class that includes functions that handle the business logics behind competition booking"""
    _MAX_PLACES_PER_COMP = 12

    def max_places_allowed(self, competition, club, max_places_per_comp=_MAX_PLACES_PER_COMP):
        """ Return the max number of places a given club can book in a given competition."""
        if club['id'] in competition:
            max_places_per_comp -= int(competition[club['id']])
        return min(int(competition['numberOfPlaces']), int(club['points']), int(max_places_per_comp))
    
    def is_competition_past(self, competition):
        """ Return true if the competition's datetime is inferior than the current datetime, meaning it's passed."""
        return datetime.fromisoformat(competition['date']) < datetime.now()