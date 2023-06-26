from utilities.json_handler import JSON_Handler

mocked_clubs = [
    {
        "id": "1",
        "name": "club_test1",
        "email": "test1@email.fr",
        "points": "30"
    },
    {
        "id": "2",
        "name": "club_test2",
        "email": "test2@email.fr",
        "points": "8"
    },
    {
        "id": "3",
        "name": "club_test3",
        "email": "test3@email.fr",
        "points": "0"
    }]

mocked_competitions = [
    {
        "name": "competition_test1",
        "date": "2025-06-22 08:00:00",
        "numberOfPlaces": "50"
    },
    {
        "name": "competition_test2",
        "date": "2034-01-01 10:00:00",
        "numberOfPlaces": "15"},
    {
        "name": "competition_test3",
        "date": "2023-11-05 09:00:00",
        "numberOfPlaces": "6"
    }]


# class JSON_mock():
#     """ Class that mocks the json files acting as database."""
#     @staticmethod
#     def mockedLoadClubs():
#         """ Mock the loadClubs method of the json_handler object"""
#         return [{"id": "1",
#                     "name": "Club Test 1",
#                     "email": "test1@email.fr",
#                     "points": "20"},
#                 {
#                     "id": "2",
#                     "name": "Club Test 2",
#                     "email": "test2@email.fr",
#                     "points": "8"},
#                 {
#                     "id": "3",
#                     "name": "Club Test 3",
#                     "email": "test3@email.fr",
#                     "points": "0"}]
#     def mockedLoadCompetitions():
#             return [{"name": "Competition Test 1",
#                      "date": "2025-06-22 08:00:00",
#                      "numberOfPlaces": "50"},
#                     {
#                      "name": "name test competition 2",
#                      "date": "2034-01-01 10:00:00",
#                      "numberOfPlaces": "15"},
#                     {
#                      "name": "name_test_competition_3",
#                      "date": "2023-11-05 09:00:00",
#                      "numberOfPlaces": "6"}]
#     @staticmethod
#     def monkeypatch_functions(monkeypatch):
#         monkeypatch.setattr(JSON_Handler, 'loadClubs', JSON_mock.mockedLoadClubs)
#         monkeypatch.setattr(JSON_Handler, 'loadCompetitions', JSON_mock.mockedLoadCompetitions)

# class MockResponse:
 
#     @staticmethod
#     def loadClubs():
#         return [{"id": "1",
#                     "name": "Club Test 1",
#                     "email": "test1@email.fr",
#                     "points": "20"},
#                 {
#                     "id": "2",
#                     "name": "Club Test 2",
#                     "email": "test2@email.fr",
#                     "points": "8"},
#                 {
#                     "id": "3",
#                     "name": "Club Test 3",
#                     "email": "test3@email.fr",
#                     "points": "0"}]
    
#     @staticmethod
#     def loadCompetitions():
#         return [{"name": "Competition Test 1",
#                      "date": "2025-06-22 08:00:00",
#                      "numberOfPlaces": "50"},
#                     {
#                      "name": "name test competition 2",
#                      "date": "2034-01-01 10:00:00",
#                      "numberOfPlaces": "15"},
#                     {
#                      "name": "name_test_competition_3",
#                      "date": "2023-11-05 09:00:00",
#                      "numberOfPlaces": "6"}]