from datetime import datetime
from pydantic import BaseModel


class SortableGameVersion(BaseModel):
    gameVersionName: str | None
    gameVersionPadded: str | None
    gameVersion: str | None
    gameVersionReleaseDate: datetime | None
    gameVersionTypeId: int | None
