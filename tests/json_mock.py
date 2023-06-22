class JSON_mock():
    """ Class that mocks the json files acting as database."""

    @staticmethod
    def mockedLoadClubs():
        """ Mock the loadClubs method of the json_handler object"""
        return [{"id": "1",
                    "name": "Club Test 1",
                    "email": "test1@email.fr",
                    "points": "20"},
                {
                    "id": "2",
                    "name": "Club Test 2",
                    "email": "test2@email.fr",
                    "points": "8"},
                {
                    "id": "3",
                    "name": "Club Test 3",
                    "email": "test3@email.fr",
                    "points": "0"}]

    def mockedLoadCompetitions():
            return [{"name": "Competition Test 1",
                     "date": "2025-06-22 08:00:00",
                     "numberOfPlaces": "50"},
                    {
                     "name": "name test competition 2",
                     "date": "2034-01-01 10:00:00",
                     "numberOfPlaces": "15"},
                    {
                     "name": "name_test_competition_3",
                     "date": "2023-11-05 09:00:00",
                     "numberOfPlaces": "6"}]


    @staticmethod
    def monkeypatch_json_functions(monkeypatch):
        monkeypatch.setattr('server.loadClubs', JSON_mock.mockedLoadClubs)
        monkeypatch.setattr('server.loadCompetitions', JSON_mock.mockedLoadCompetitions)
