from datetime import datetime
from pydantic import BaseModel
from ..categories import Category
from .mod_author import ModAuthor
from .mod_file import ModFile
from .mod_file_index import ModFileIndex
from .mod_info_links import ModInfoLinks
from .mod_logo import ModLogo
from .mod_screenshot import ModScreenshot


class ModInfo(BaseModel):
    id: int | None
    gameId: int | None
    name: str | None
    slug: str | None
    links: ModInfoLinks | None
    summary: str | None
    status: int | None
    downloadCount: int | None
    isFeatured: bool | None
    primaryCategoryId: int | None
    categories: list[Category] | None
    classId: int | None
    authors: list[ModAuthor] | None
    logo: ModLogo | None
    screenshots: list[ModScreenshot] | None
    mainFileId: int | None
    latestFiles: list[ModFile] | None
    latestFilesIndexes: list[ModFileIndex] | None
    dateCreated: datetime | None
    dateModified: datetime | None
    dateReleased: datetime | None
    allowModDistribution: bool | None
    gamePopularityRank: int | None
    isAvailable: bool | None
    thumbsUpCount: int | None
