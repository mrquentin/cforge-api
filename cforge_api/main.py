from pprint import pprint

from pydantic import BaseModel, HttpUrl
from uplink import Consumer, returns, get

from cforge_api.client import CForgeAPI


class Owner(BaseModel):
    id: int
    avatar_url: HttpUrl
    organizations_url: HttpUrl


class Repo(BaseModel):
    id: int
    full_name: str
    owner: Owner


class Github(Consumer):
    @returns.json()
    @get("users/{username}/repos")
    def get_repos(self, username) -> list[Repo]: pass

    @returns.json()
    @get("users/{username}/repos")
    def get_repos_json(self, username): pass


def run():
    api = CForgeAPI("$2a$10$t0XXH1pJ8ZvcGeZtBeQ0nulnjrAOy/OzZewuWqX2dxslbEdYDrP/6")
    pprint(api.get_game_by_id(432))


if __name__ == "__main__":
    run()
