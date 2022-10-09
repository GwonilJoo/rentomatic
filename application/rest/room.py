import json
import mimetypes

from flask import Blueprint, Response

from rentomatic.repository.memrepo import MemRepo
from rentomatic.use_cases.room_list import room_list_use_case
from rentomatic.serializers.room import RoomJsonEncoder


blueprint = Blueprint("room", __name__)


rooms = [
    {
        "code": "a853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 100,
        "price": 19,
        "longitude": -0.1999943,
        "latitude": 11.5643634634,
    },
    {
        "code": "b853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 200,
        "price": 29,
        "longitude": -0.2999943,
        "latitude": 21.5643634634,
    },
    {
        "code": "c853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 300,
        "price": 39,
        "longitude": -0.3999943,
        "latitude": 31.5643634634,
    },
    {
        "code": "d853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 400,
        "price": 49,
        "longitude": -0.4999943,
        "latitude": 41.5643634634,
    },
]


@blueprint.route("/rooms", methods=["GET"])
def room_list():
    repo = MemRepo(rooms)
    result = room_list_use_case(repo)

    return Response(
        json.dumps(result, cls=RoomJsonEncoder),
        mimetype="application/json",
        status=200,
    )