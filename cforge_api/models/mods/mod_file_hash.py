from pydantic import BaseModel


class ModFileHash(BaseModel):
    value: str | None
    algo: int | None
