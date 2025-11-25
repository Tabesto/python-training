# repositories/base.py
from typing import Dict, Generic, TypeVar, List, Optional

T = TypeVar("T")

class InMemoryRepository(Generic[T]):
    def __init__(self) -> None:
        self._items: Dict[int, T] = {}
        self._next_id: int = 1

    def list(self) -> List[T]:
        return list(self._items.values())

    def get(self, item_id: int) -> Optional[T]:
        return self._items.get(item_id)

    def create(self, item: T) -> T:
        # On suppose que T a un attribut "id"
        setattr(item, "id", self._next_id)
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def update(self, item_id: int, item: T) -> Optional[T]:
        if item_id not in self._items:
            return None
        setattr(item, "id", item_id)
        self._items[item_id] = item
        return item

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None
