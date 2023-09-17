from fastapi import FastAPI
from app.domain import CharCounter

from app.dto import ResponseDto, CommandDto


app = FastAPI()


@app.post("/do-thing", response_model=ResponseDto)
def do_a_thing_url_command(command: CommandDto):
    command_string = command.command

    character_counter = CharCounter(input=command_string)

    char_counts = character_counter.count_characters()

    first_character = command_string[0]

    first_character_counts = [
        char_count for char_count in char_counts if char_count.char == first_character
    ]

    return ResponseDto(input=command, count=first_character_counts[0].count)
