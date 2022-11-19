from pydantic import BaseModel


class GameInfoAssets(BaseModel):
    coverUrl: str | None
    iconUrl: str | None
    titleUrl: str | None
