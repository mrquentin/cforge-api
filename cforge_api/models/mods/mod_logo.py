from pydantic import BaseModel


class ModLogo(BaseModel):
    id: int | None
    url: str | None
    thumbnailUrl: str | None
