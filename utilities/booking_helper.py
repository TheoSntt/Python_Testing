from datetime import datetime

class Booking_Helper:
    """Utility class that includes functions that handle the business logics behind competition booking"""
    
    def max_places_allowed(self, competition, club, max_places_per_comp):
        """ Return the max number of places a given club can book in a given competition."""
        if club['id'] in competition:
            print(competition)
            max_places_per_comp -= int(competition[club['id']])
        print(max_places_per_comp)
        return min(int(competition['numberOfPlaces']), int(club['points']), int(max_places_per_comp))
    
    def is_competition_passed(self, competition):
        """ Return true if the competition's datetime is inferior than the current datetime, meaning it's passed."""
        return datetime.fromisoformat(competition['date']) < datetime.now()