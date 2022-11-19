from datetime import datetime
from pydantic import BaseModel

from cforge_api.models import SortableGameVersion
from cforge_api.models.mods.mod_dependency import ModDependency
from cforge_api.models.mods.mod_file_hash import ModFileHash
from cforge_api.models.mods.mod_module import ModModule


class ModFile(BaseModel):
    id: int | None
    gameId: int | None
    modId: int | None
    isAvailable: bool | None
    displayName: str | None
    fileName: str | None
    releaseType: int | None
    fileStatus: int | None
    hashes: list[ModFileHash] | None
    fileDate: datetime | None
    fileLength: int | None
    downloadCount: int | None
    downloadUrl: str | None
    gameVersions: list[str] | None
    sortableGameVersions: list[SortableGameVersion] | None
    dependencies: list[ModDependency] | None
    exposeAsAlternative: bool | None
    parentProjectFileId: int | None
    alternativeFileId: int | None
    isServerPack: bool | None
    serverPackFileId: int | None
    fileFingerprint: int | None
    modules: list[ModModule] | None
