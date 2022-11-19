from uplink import Consumer, get, returns, QueryMap, post, Body, json
from .models import *


class CForgeAPI(Consumer):

    def __init__(self, api_key: str):
        super(CForgeAPI, self).__init__(base_url="https://api.curseforge.com")
        self.session.headers['Accept'] = 'application/json'
        self.session.headers['x-api-key'] = api_key

    # Games
    @returns.json(key="data")
    @get("/v1/games")
    def get_games(self) -> list[GameInfo]:
        """Get all games that are available to the provided API key"""

    @returns.json(key="data")
    @get("/v1/games/{gameId}")
    def get_game_by_id(self, gameId: int) -> GameInfo:
        """Get a single game. A private game is only accessible by its respective API key"""

    @returns.json(key="data")
    @get("/v1/games/{gameId}/versions")
    def get_game_versions(self, gameId: int) -> list[GameVersion]:
        """Get all available versions for each known version type of the specified game"""

    @returns.json(key="data")
    @get("/v1/games/{gameId}/version-types")
    def get_game_versions_types(self, gameId: int) -> list[GameVersionType]:
        """Get all available version types of the specified game"""

    # Category
    @returns.json(key="data")
    @get("/v1/categories")
    def __get_categories(self, **params: QueryMap) -> list[Category]:
        """Get all available classes and categories of the specified game.
        Specify a game id for a list of all game categories, or a class id for a list of categories under that class.
        Specify the classes Only flag to just get the classes for a given game"""

    def get_categories(self, gameId: int, classId: int = None, classesOnly: bool = False) -> list[Category]:
        """Get all available classes and categories of the specified game.
        Specify a game id for a list of all game categories, or a class id for a list of categories under that class.
        Specify the classes Only flag to just get the classes for a given game"""
        params = {k: v for k, v in locals().items() if v is not None and v != self}
        return self.__get_categories(**params)

    # Mods
    @returns.json()
    @get("/v1/mods/search")
    def __search_mods(self, **params: QueryMap) -> ModSearchResult:
        """Get all mods that match the search criteria.
        Specify a category id to limit the search to a specific category.
        Specify a sort option to sort the results. The default is relevance.
        Specify a limit to limit the number of results. The default is 25.
        Specify an index to start at a specific result. The default is 0."""

    def search_mods(self, gameId: int, classId: int = None, categoryId: int = None, gameVersion: str = None,
                    searchFilter: str = None, sortField: ModSearchSortField = None,
                    sortOrder: SortOrder = None, modLoaderType: ModLoaderType = None,
                    gameVersionTypeId: int = None, slug: str = None, index: int = None,
                    pageSize: int = None) -> ModSearchResult:
        params = {}
        for k, v in locals().items():
            if isinstance(v, Enum) and v is not None:
                params[k] = v.value
            elif v is not None and v != self:
                params[k] = v

        return self.__search_mods(**params)

    @returns.json(key="data")
    @get("/v1/mods/{modId}")
    def get_mod_by_id(self, modId: int) -> ModInfo:
        """Get a single mod"""

    # @json
    @returns.json(key="data")
    @post("/v1/mods/")
    def get_mods_by_id(self, modIds: Body) -> list[ModInfo]:
        """Get a list of mods"""
