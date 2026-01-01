from typing import Annotated
from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("")
def list_items():
    return ["item1", "item2", "item3", "item4", "item5", "item6"]


@router.get("/{item_id}")
def get_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item_id": item_id}
