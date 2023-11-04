from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix='/items', tags=["items"])


@router.get('')
def list_items():
    return [
        "Item1",
        "Item2",
        "item3",
        "Item4"
    ]

@router.get('/latest')
def get_latest_tems():
    return {"item":{"id": "13", "name":"latest"}}

@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000)]):
    return {
        "item": {
            "id": item_id
        } 
    }
