from __future__ import annotations
from abc import ABC, abstractmethod
from json import dumps

from matrix_sum.matrix import ABCMinimalMatrix


class ABCFormat(ABC):
    @abstractmethod
    def __call__(self) -> str:
        pass


class JsonFormat(ABCFormat):
    def __init__(self, matrix: ABCMinimalMatrix) -> None:
        self._matrix = matrix

    def __call__(self) -> str:
        matrix_like = list()
        for i in range(0, self._matrix.get_shape()[0]):
            row_like = list()
            for j in range(0, self._matrix.get_shape()[1]):
                row_like.append(self._matrix.get_cell(i, j))
            matrix_like.append(row_like)
        return dumps(matrix_like)


class ABCFormatFactory(ABC):
    @abstractmethod
    def __call__(self) -> ABCFormat:
        pass


class JsonFormatFactory(ABC):
    def __init__(self, matrix: ABCMinimalMatrix) -> None:
        self._matrix = matrix

    def __call__(self) -> ABCFormat:
        return JsonFormat(matrix=self._matrix)
