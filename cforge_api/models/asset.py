from pydantic import BaseModel

class Asset(BaseModel):
    name: str
    url: str
