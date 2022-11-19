from datetime import datetime
from pydantic import BaseModel
from .game_info_asset import GameInfoAssets


class GameInfo(BaseModel):
    id: int | None
    name: str | None
    slug: str | None
    date_modified: datetime | None
    assets: GameInfoAssets | None
    status: int | None
    api_status: int | None
