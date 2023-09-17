from pydantic import BaseModel, Field


class CharCount(BaseModel):
    char: str = Field(max_length=1)
    count: int


class CharCounter(BaseModel):
    input: str

    def count_characters(self) -> list[CharCount]:
        character_counts = []
        unique_characters = set(self.input)
        for character in unique_characters:
            character_count = CharCount(
                char=character, count=self.input.count(character)
            )
            character_counts.append(character_count)

        return character_counts
