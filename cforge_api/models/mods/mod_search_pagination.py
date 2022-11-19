from pydantic import BaseModel


class ModSearchPagination(BaseModel):
    index: int | None
    pageSize: int | None
    resultCount: int | None
    totalCount: int | None
