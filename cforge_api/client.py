from uplink import Consumer, get, returns, QueryMap
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
    @get("/v1/games/{game_id}")
    def get_game_by_id(self, game_id: int) -> GameInfo:
        """Get a single game. A private game is only accessible by its respective API key"""

    @returns.json(key="data")
    @get("/v1/games/{game_id}/versions")
    def get_game_versions(self, game_id: int) -> list[GameVersion]:
        """Get all available versions for each known version type of the specified game"""

    @returns.json(key="data")
    @get("/v1/games/{game_id}/version-types")
    def get_game_versions_types(self, game_id: int) -> list[GameVersionType]:
        """Get all available version types of the specified game"""

    # Category
    @returns.json(key="data")
    @get("/v1/categories")
    def __get_categories(self, **params: QueryMap) -> list[Category]:
        """Get all available classes and categories of the specified game.
        Specify a game id for a list of all game categories, or a class id for a list of categories under that class.
        Specify the classes Only flag to just get the classes for a given game"""

    def get_categories(self, game_id: int, class_id: int = None, classes_only: bool = False) -> list[Category]:
        """Get all available classes and categories of the specified game.
        Specify a game id for a list of all game categories, or a class id for a list of categories under that class.
        Specify the classes Only flag to just get the classes for a given game"""
        params = {'gameId': game_id}
        if class_id is not None:
            params['classId'] = class_id
        if classes_only:
            params['classesOnly'] = classes_only
        return self.__get_categories(**params)
