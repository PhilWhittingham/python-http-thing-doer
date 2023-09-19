import json
from pydantic import BaseModel


class MockDatabaseClient(BaseModel):
    datastore: list[str] = []

    def insert_one(self, inserted_one: dict):
        # We cheat here to do the serialisation which may
        # be handled by the database engine
        serialised_inserted_one = json.dumps(inserted_one)

        self.datastore.append(serialised_inserted_one)

    def find(self, query_dict: dict):
        # Only support minimum query here for the test
        request_input = query_dict["request_input"]

        matched_data: list[dict] = []
        for data in self.datastore:
            json_data = json.loads(data)
            if json_data["request_input"] != request_input:
                continue

            matched_data.append(json_data)

        return matched_data
