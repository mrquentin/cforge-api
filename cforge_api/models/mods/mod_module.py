from pydantic import BaseModel


class ModModule(BaseModel):
    name: str | None
    fingerprint: int | None
