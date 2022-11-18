from marshmallow import Schema, fields
from . import Asset


class GameInfo(BaseModel):
    id: int
    name: str
    slug: str
    date_modified: datetime
    assets: List[Asset]
    status: int
    api_status: int
