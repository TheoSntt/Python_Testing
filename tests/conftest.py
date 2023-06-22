import pytest
from unittest.mock import patch

from utilities.json_handler import JSON_Handler
from server import create_app
from tests.json_mock import mocked_clubs, mocked_competitions


# @pytest.fixture
# def patch_json(monkeypatch):
#     JSON_mock.monkeypatch_functions(monkeypatch)

@pytest.fixture
def client():
    with patch.object(JSON_Handler, 'loadClubs') as mock_load_clubs, patch.object(JSON_Handler, 'loadCompetitions') as mock_load_competitions:
        # Mock the return values of the methods
        mock_load_clubs.return_value = mocked_clubs
        mock_load_competitions.return_value = mocked_competitions
        app = create_app({"TESTING": True})
        with app.test_client() as client:
            yield client