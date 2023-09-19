import logging
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from app.domain import CharCounter

from app.dto import ResponseDto, CommandDto
from app.exceptions import CountNotFoundException
from app.repository import CharacterCountRepository

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/do-thing", response_model=ResponseDto)
@inject
def do_a_thing_url_command(
    command: CommandDto,
    repository: CharacterCountRepository = Depends(Provide[Container.count_repository]),
):
    command_string = command.command
    first_character = command_string[0]
    logger.info(f"Request received to count command: {command_string}")

    logger.debug("Attempting to avoid calculation by checking database")
    try:
        count = repository.get_count(first_character, command_string)
        logger.info(f"Returning retrieved value: {count}")
        return ResponseDto(input=command, count=count)
    except CountNotFoundException:
        logger.debug("Unable to find result in database, proceeding to calculation")

    character_counter = CharCounter(input=command_string)
    char_counts = character_counter.count_characters()

    first_character_counts = [
        char_count for char_count in char_counts if char_count.char == first_character
    ]

    first_character_count = first_character_counts[0]

    logger.debug(f"Successfully calculated count of {first_character_count.count}")
    repository.save_count(first_character_count, command_string)
    logger.debug("Saved count in database")

    logger.info(f"Returning calculated value: {first_character_count.count}")
    return ResponseDto(input=command, count=first_character_counts[0].count)
