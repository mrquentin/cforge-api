from datetime import datetime
from pydantic import BaseModel


class Category(BaseModel):
    id: int | None
    gameId: int | None
    name: str | None
    slug: str | None
    url: str | None
    iconUrl: str | None
    dateModified: datetime | None
    isClass: bool | None
    classId: int | None
    parentCategoryId: int | None
    displayIndex: int | None
