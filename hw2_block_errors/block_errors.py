from typing import Collection, Type, Literal
from types import TracebackType

class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.errors = tuple(errors)

    def __enter__(self):
        return None

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if exc_type and issubclass(exc_type, self.errors):
            return True
        return None
