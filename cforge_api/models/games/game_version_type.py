from pydantic import BaseModel


class GameVersionType(BaseModel):
    id: int | None
    gameId: int | None
    name: str | None
    slug: str | None
