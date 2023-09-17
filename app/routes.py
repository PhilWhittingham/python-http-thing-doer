from fastapi import FastAPI

from app.dto import ResponseDto, CommandDto


app = FastAPI()


@app.post("/do-thing", response_model=ResponseDto)
def do_a_thing_url_command(command: CommandDto):
    return ResponseDto(input=command, count=0)
