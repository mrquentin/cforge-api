from pydantic import BaseModel


class ModAuthor(BaseModel):
    id: int | None
    modId: int | None
    title: str | None
    description: str | None
    thumbnailUrl: str | None
    url: str | None
