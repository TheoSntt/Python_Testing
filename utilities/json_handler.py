import json


class JSON_Handler:
    """Utility class to handle JSON reading and writing"""

    # def load_clubs(self):
    #     """Load the clubs from the clubs JSON file"""
    #     with open('./db/clubs.json') as c:
    #         listOfClubs = json.load(c)['clubs']
    #         return listOfClubs


    # def load_competitions(self):
    #     """Load the competitions from the competitions JSON file"""
    #     with open('./db/competitions.json') as comps:
    #         listOfCompetitions = json.load(comps)['competitions']
    #         return listOfCompetitions
    
    def load_json(self, file_name):
        """ Load the data from the JSON file passed as parameter """
        with open(f'db/{file_name}.json') as file:
            return json.load(file)[file_name]
    
    def save_json(self, file_name, data):
        """ Open the file db/file_name.json with the list of dicts 'data'
            This list will be saved in a dict, in the field {file_name} """
        with open(f'db/{file_name}.json', 'w') as file:
            json.dump({file_name: data}, file, indent=True)
    
    def update_json(self, file_name, data):
        """ Update an entry in the '/db/file_name.json and save the file. """
        tab = self.load_json(file_name)
        for entry in tab:
            if entry['name'] == data['name']:
                tab.remove(entry)
                break

        tab.insert(0, data)
        self.save_json(file_name, tab)



