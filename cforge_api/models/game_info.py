from datetime import datetime
from pydantic import BaseModel, HttpUrl, validator


class GameInfoAssets(BaseModel):
    coverUrl: str | None
    iconUrl: str | None
    titleUrl: str | None


class GameInfo(BaseModel):
    id: int | None
    name: str | None
    slug: str | None
    date_modified: datetime | None
    assets: GameInfoAssets | None
    status: int | None
    api_status: int | None
