from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from json import loads

from numpy.typing import ArrayLike


class ABCParser(ABC):
    @abstractmethod
    def __call__(self) -> List[ArrayLike]:
        pass


class JsonParser(ABC):
    def __init__(self, content: str) -> None:
        self._content = content

    def __call__(self) -> List[ArrayLike]:
        parsed_content = loads(self._content)
        matrix1 = parsed_content["a"]
        matrix2 = parsed_content["b"]
        return [matrix1, matrix2]


class ABCParserFactory(ABC):
    @abstractmethod
    def __call__(self, content: str) -> ABCParser:
        pass


class JsonParserFactory(ABCParserFactory):
    def __call__(self, content: str) -> ABCParser:
        return JsonParser(content=content)
