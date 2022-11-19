from pydantic import BaseModel


class ModInfoLinks(BaseModel):
    websiteUrl: str | None
    wikiUrl: str | None
    issuesUrl: str | None
    sourceUrl: str | None
