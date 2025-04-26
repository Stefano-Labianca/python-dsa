from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> T | None:
        if self.is_empty():
            return None
        
        return self.items[-1]

    def pop(self) -> T | None:
        if self.is_empty():
            return None
        
        return self.items.pop()

    def is_empty(self) -> bool:
        return self.size() == 0