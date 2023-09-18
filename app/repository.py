from typing import Any

from pydantic import BaseModel

from app.domain import CharCount
from app.exceptions import CountNotFoundException


class CharacterCountRepository(BaseModel):
    # Ignore typing for this example, but imagine this could be
    # your typical pymongo collection or some sqlalchemy construct
    # which allows for saving and retrieving
    client: Any

    def get_count(self, character: str, request_input: str) -> int:
        database_counts = self.client.find({"request_input": request_input})

        for database_count in database_counts:
            if database_count["count"]["char"] != character:
                continue

            return database_count["count"]["count"]

        raise CountNotFoundException()

    def save_count(self, character_count: CharCount, request_input: str):
        database_character_count = {
            "count": character_count,
            "request_input": request_input,
        }
        self.client.insert_one(database_character_count)
