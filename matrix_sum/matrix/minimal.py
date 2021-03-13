from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple

from numpy import array
from numpy.typing import ArrayLike


class ABCMinimalMatrix(ABC):
    @abstractmethod
    def get_cell(self, row_index: int, column_index: int) -> int:
        pass

    @abstractmethod
    def get_shape(self) -> Tuple[int, int]:
        pass


class MinimalMatrix(ABCMinimalMatrix):
    def __init__(self, matrix_like: ArrayLike):
        self._matrix = array(matrix_like)
    
    def get_cell(self, row_index: int, column_index: int) -> int:
        return self._matrix[row_index][column_index]
    
    def get_shape(self) -> Tuple[int, int]:
        return self._matrix.shape


class ABCMinimalMatrixFactory(ABC):
    @abstractmethod
    def __call__(self, matrix_like: ArrayLike) -> ABCMinimalMatrix:
        pass


class MinimalMatrixFactory(ABCMinimalMatrixFactory):
    def __call__(self, matrix_like: ArrayLike) -> ABCMinimalMatrix:
        return MinimalMatrix(matrix_like=matrix_like)
