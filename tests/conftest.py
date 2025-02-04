import pytest
from unittest.mock import patch

from utilities.json_handler import JSON_Handler
from server import create_app
from tests.json_mock import mock_load_json, mock_update_json


@pytest.fixture
def client():
    with patch.object(JSON_Handler, 'load_json') as mocked_load, patch.object(JSON_Handler, 'update_json') as mocked_update:
        mocked_load.side_effect = mock_load_json
        mocked_update.side_effect = mock_update_json
        app = create_app({"TESTING": True})
        with app.test_client() as client:
            yield client

