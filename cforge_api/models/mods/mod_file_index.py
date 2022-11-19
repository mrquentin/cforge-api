from pydantic import BaseModel


class ModFileIndex(BaseModel):
    gameVersion: str | None
    fileId: int | None
    filename: str | None
    releaseType: int | None
    gameVersionTypeId: int | None
    modLoader: int | None
