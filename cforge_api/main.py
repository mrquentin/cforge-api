from pprint import pprint
from cforge_api.client import CForgeAPI

from cforge_api.models import GetModsByIdsRequestBody


def run():
    # Minecraft id = 432
    api = CForgeAPI("$2a$10$t0XXH1pJ8ZvcGeZtBeQ0nulnjrAOy/OzZewuWqX2dxslbEdYDrP/6")
    # pprint(list(map(lambda x: x.name, api.search_mods(432, searchFilter="Vault").data)))
    ids = {"modIds": [1, 2, 3]}
    # pprint(api.get_mods_by_ids(ids))
    pprint(api.get_games())


if __name__ == "__main__":
    run()

