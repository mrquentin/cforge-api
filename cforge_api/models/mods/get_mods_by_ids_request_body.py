from pydantic import BaseModel


class GetModsByIdsRequestBody(BaseModel):
    modIds: list[int]
