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

@staticmethod
def mock_load_json(file_name):
    if 'clubs' in file_name:
        return mocked_clubs
    elif 'competitions' in file_name:
        return mocked_competitions
    else:
        return []

@staticmethod
def mock_update_json(file_name, data):
    pass
