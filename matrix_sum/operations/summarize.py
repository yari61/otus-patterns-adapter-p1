from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, final
from functools import reduce

from numpy import zeros

from matrix_sum.matrix import ABCMinimalMatrix, ABCMinimalMatrixFactory


class ABCSummarize(ABC):
    @abstractmethod
    def __call__(self) -> ABCMinimalMatrix:
        pass


@final
class SummarizePair(ABCSummarize):
    __slots__ = ["_matrix1", "_matrix2", "_matrix_factory"]

    def __init__(self, matrix1: ABCMinimalMatrix, matrix2: ABCMinimalMatrix, matrix_factory: ABCMinimalMatrixFactory) -> None:
        self._matrix1 = matrix1
        self._matrix2 = matrix2
        self._matrix_factory = matrix_factory

    def __call__(self) -> ABCMinimalMatrix:
        matrix_like = zeros(shape=self._matrix1.get_shape())
        for row_index in range(0, self._matrix1.get_shape()[0]):
            for column_index in range(0, self._matrix1.get_shape()[1]):
                matrix_like[row_index][column_index] = self._matrix1.get_cell(row_index, column_index) + self._matrix2.get_cell(row_index, column_index)
        return self._matrix_factory(matrix_like=matrix_like)


class ABCSummarizePairFactory(ABC):
    @abstractmethod
    def __call__(self, matrix1: ABCMinimalMatrix, matrix2: ABCMinimalMatrix) -> ABCSummarize:
        pass


class SummarizePairFactory(ABC):
    def __init__(self, matrix_factory: ABCMinimalMatrixFactory) -> None:
        self._matrix_factory = matrix_factory

    def __call__(self, matrix1: ABCMinimalMatrix, matrix2: ABCMinimalMatrix) -> ABCSummarize:
        return SummarizePair(matrix1=matrix1, matrix2=matrix2, matrix_factory=self._matrix_factory)


@final
class Summarize(ABCSummarize):
    __slots__ = ["_matrices", "_summarize_pair_factory"]

    def __init__(self, matrices: Iterable[ABCMinimalMatrix], summarize_pair_factory: ABCSummarizePairFactory) -> None:
        self._matrices = matrices
        self._summarize_pair_factory = summarize_pair_factory

    def __call__(self) -> ABCMinimalMatrix:
        return reduce(lambda m1, m2: self._summarize_pair_factory(matrix1=m1, matrix2=m2).__call__(), self._matrices)
