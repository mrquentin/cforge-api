from pydantic import BaseModel


class GameVersionType(BaseModel):
    id: int
    gameId: int
    name: str
    slug: str
