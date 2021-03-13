from __future__ import annotations
from abc import ABC, abstractmethod
from json import dumps

from matrix_sum.matrix import ABCMinimalMatrix
from matrix_sum.matrix.extensions import ToList


class ABCFormat(ABC):
    @abstractmethod
    def __call__(self) -> str:
        pass


class JsonFormat(ABCFormat):
    def __init__(self, matrix: ABCMinimalMatrix) -> None:
        self._matrix = matrix

    def __call__(self) -> str:
        to_list = ToList(matrix=self._matrix)
        matrix_like = to_list()
        return dumps(matrix_like)


class ABCFormatFactory(ABC):
    @abstractmethod
    def __call__(self) -> ABCFormat:
        pass


class JsonFormatFactory(ABCFormatFactory):
    def __init__(self, matrix: ABCMinimalMatrix) -> None:
        self._matrix = matrix

    def __call__(self) -> ABCFormat:
        return JsonFormat(matrix=self._matrix)
