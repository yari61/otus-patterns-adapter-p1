from __future__ import annotations
from abc import ABC, abstractmethod

from numpy import array
from numpy.typing import ArrayLike

from .minimal import ABCMinimalMatrix


class ABCEqual(ABC):
    __slots__ = ["_matrix1", "_matrix2"]

    def __init__(self, matrix1: ABCMinimalMatrix, matrix2: ABCMinimalMatrix) -> None:
        self._matrix1 = matrix1
        self._matrix2 = matrix2
    
    @abstractmethod
    def __call__(self) -> bool:
        pass


class Equal(ABCEqual):
    def __call__(self) -> bool:
        if not self._matrix1.get_shape() == self._matrix2.get_shape():
            return False
        for i in range(0, self._matrix1.get_shape()[0]):
            for j in range(0, self._matrix1.get_shape()[1]):
                if not self._matrix1.get_cell(i, j) == self._matrix2.get_cell(i, j):
                    return False
        return True


class ABCGetRow(ABC):
    __slots__ = ["_matrix", "_index"]

    def __init__(self, matrix: ABCMinimalMatrix, index: int) -> None:
        self._matrix = matrix
        self._index = index
    
    @abstractmethod
    def __call__(self) -> ArrayLike:
        pass


class GetRow(ABCGetRow):
    def __call__(self) -> ArrayLike:
        row_length = self._matrix.get_shape()[1]
        return array([self._matrix.get_cell(self._index, i) for i in range(0, row_length)])


class ABCGetColumn(ABC):
    __slots__ = ["_matrix", "_index"]

    def __init__(self, matrix: ABCMinimalMatrix, index: int) -> None:
        self._matrix = matrix
        self._index = index
    
    @abstractmethod
    def __call__(self) -> ArrayLike:
        pass


class GetColumn(ABCGetColumn):
    def __call__(self) -> ArrayLike:
        column_length = self._matrix.get_shape()[0]
        return array([self._matrix.get_cell(i, self._index) for i in range(0, column_length)])
