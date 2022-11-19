from pydantic import BaseModel


class GameVersion(BaseModel):
    type: int | None
    versions: list[str] | None
