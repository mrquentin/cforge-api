from datetime import datetime
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    gameId: int
    name: str
    slug: str
    url: str
    iconUrl: str
    dateModified: datetime
    isClass: bool
    classId: int
    parentCategoryId: int
    displayIndex: int
