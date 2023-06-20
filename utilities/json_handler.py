import json


class JSON_Handler:
    """Utility class to handle JSON reading and writing"""

    def loadClubs(self):
        """Load the clubs from the clubs JSON file"""
        with open('./db/clubs.json') as c:
            listOfClubs = json.load(c)['clubs']
            return listOfClubs


    def loadCompetitions(self):
        """Load the competitions from the competitions JSON file"""
        with open('./db/competitions.json') as comps:
            listOfCompetitions = json.load(comps)['competitions']
            return listOfCompetitions



