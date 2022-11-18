from datetime import datetime
from pprint import pprint

from marshmallow import Schema, fields
from cforge_api.client import CForgeAPI


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Str()


class BlogSchema(Schema):
    title = fields.Str()
    author = fields.Nested(UserSchema)

def run():
    api = CForgeAPI("$2a$10$t0XXH1pJ8ZvcGeZtBeQ0nulnjrAOy/OzZewuWqX2dxslbEdYDrP/6")
    games = api.get_games()
    pprint(games)


if __name__ == "__main__":
    run()
