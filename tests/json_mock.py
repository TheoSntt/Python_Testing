from utilities.json_handler import JSON_Handler
import json

# mocked_clubs = [
#     {
#         "id": "1",
#         "name": "club_test1",
#         "email": "test1@email.fr",
#         "points": "30"
#     },
#     {
#         "id": "2",
#         "name": "club_test2",
#         "email": "test2@email.fr",
#         "points": "8"
#     },
#     {
#         "id": "3",
#         "name": "club_test3",
#         "email": "test3@email.fr",
#         "points": "0"
#     }]

# mocked_competitions = [
#     {
#         "name": "competition_test1",
#         "date": "2025-06-22 08:00:00",
#         "numberOfPlaces": "50"
#     },
#     {
#         "name": "competition_test2",
#         "date": "2034-01-01 10:00:00",
#         "numberOfPlaces": "15"},
#     {
#         "name": "competition_test3",
#         "date": "2023-11-05 09:00:00",
#         "numberOfPlaces": "6"
#     },
#     {
#         "name": "competition_test4",
#         "date": "2020-11-05 09:00:00",
#         "numberOfPlaces": "6000"
#     }]
def load_mocked_json_data(file_name):
    """ Retrieve the test data from their respective JSON files """
    with open(f'tests/mocked_{file_name}.json') as file:
        return json.load(file)['mocked_' + file_name]


def mock_load_json(file_name):
    if 'clubs' in file_name:
        return load_mocked_json_data(file_name)
    elif 'competitions' in file_name:
        return load_mocked_json_data(file_name)
    else:
        return []


def mock_update_json(file_name, data):
    pass