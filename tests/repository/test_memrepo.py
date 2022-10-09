import pytest
import uuid

from rentomatic.domain.room import Room
from rentomatic.repository.memrepo import MemRepo


@pytest.fixture
def room_dicts():
    return [
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


def test_repository_list_without_parameters(room_dicts):
    repo = MemRepo(room_dicts)

    rooms = [Room.from_dict(i) for i in room_dicts]

    assert repo.list() == rooms