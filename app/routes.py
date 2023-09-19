from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from app.domain import CharCounter

from app.dto import ResponseDto, CommandDto
from app.repository import CharacterCountRepository


router = APIRouter()


@router.post("/do-thing", response_model=ResponseDto)
@inject
def do_a_thing_url_command(
    command: CommandDto,
    repository: CharacterCountRepository = Depends(Provide[Container.count_repository]),
):
    command_string = command.command

    character_counter = CharCounter(input=command_string)

    char_counts = character_counter.count_characters()

    first_character = command_string[0]

    first_character_counts = [
        char_count for char_count in char_counts if char_count.char == first_character
    ]

    first_character_count = first_character_counts[0]
    repository.save_count(first_character_count, command_string)

    return ResponseDto(input=command, count=first_character_counts[0].count)
