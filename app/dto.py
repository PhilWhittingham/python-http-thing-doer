from pydantic import BaseModel


class CommandDto(BaseModel):
    command: str
    
class ResponseDto(BaseModel):
    input: CommandDto
    count: int
