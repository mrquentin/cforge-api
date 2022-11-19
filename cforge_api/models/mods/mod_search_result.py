from pydantic import BaseModel

from .mod_info import ModInfo
from .mod_search_pagination import ModSearchPagination


class ModSearchResult(BaseModel):
    data: list[ModInfo] | None
    pagination: ModSearchPagination | None
