from pydantic import BaseModel


class ModDependency(BaseModel):
    modId: int | None
    relationType: int | None
