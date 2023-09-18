from unittest.mock import MagicMock

import pytest
from app.domain import CharCount
from app.exceptions import CountNotFoundException
from app.repository import CharacterCountRepository


def test_character_count_repository_save_with_inputs_returns_none():
    char_count = CharCount(char="t", count=1)
    request_input = "this"

    mocked_client = MagicMock()
    mocked_client.insert_one.return_value = None
    repository = CharacterCountRepository(client=mocked_client)

    # We assert the function completed successfully
    assert repository.save_count(char_count, request_input) is None


def test_character_count_repository_get_with_count_present_returns_count_value():
    mocked_client = MagicMock()
    mocked_client.find.return_value = [
        {"request_input": "this", "count": {"char": "t", "count": 1}}
    ]
    repository = CharacterCountRepository(client=mocked_client)

    count = repository.get_count("t", "this")

    assert count == 1


def test_character_count_repository_get_with_count_missing_raises_exception():
    mocked_client = MagicMock()
    mocked_client.find.return_value = []
    repository = CharacterCountRepository(client=mocked_client)

    with pytest.raises(CountNotFoundException):
        _ = repository.get_count("t", "this")
