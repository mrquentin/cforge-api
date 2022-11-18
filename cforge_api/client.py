from uplink import Consumer, get, returns
from .models import GameInfo


class CForgeAPI(Consumer):

    def __init__(self, api_key: str):
        super(CForgeAPI, self).__init__(base_url="https://api.curseforge.com")
        self.session.headers['Accept'] = 'application/json'
        self.session.headers['x-api-key'] = api_key

    # @returns.json(key="data")
    @returns.json(key="data")
    @get("/v1/games")
    def get_games(self) -> list[GameInfo]: pass

    @returns.json(key="data")
    @get("/v1/games/{game_id}")
    def get_game_by_id(self, game_id: int) -> GameInfo: pass
