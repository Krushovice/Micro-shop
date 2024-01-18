from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/items", tags=['items'])


@router.get("/")
def read_items():
    return [
        {"id": 1,
         "name": "item1",
         },
        {"id": 2,
         "name": "item2",
         },
        {"id": 3,
         "name": "item3",
         },
    ]


@router.get("/{item_id}")
def get_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }
