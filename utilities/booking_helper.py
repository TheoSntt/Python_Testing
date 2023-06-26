class Booking_Helper:
    """Utility class that includes functions that handle the business logics behind competition booking"""
    
    def max_places_allowed(self, competition, club, max_places_per_comp):
        """ Return the max number of places a given club can book in a given competition."""
        return min(int(competition['numberOfPlaces']), int(club['points']), int(max_places_per_comp))