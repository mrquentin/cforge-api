from pydantic import BaseModel


class GameVersion(BaseModel):
    type: int
    versions: list[str]
