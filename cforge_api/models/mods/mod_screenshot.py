from pydantic import BaseModel


class ModScreenshot(BaseModel):
    id: int | None
    modId: int | None
    title: str | None
    description: str | None
    thumbnailUrl: str | None
    url: str | None
