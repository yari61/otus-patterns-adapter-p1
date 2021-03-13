from __future__ import annotations
from abc import ABC, abstractmethod
from typing import final

from .format import ABCFormatFactory
from .write import ABCWriteFactory
from matrix_sum.matrix import ABCMinimalMatrix


@final
class MatrixDump(ABC):
    __slots__ = ["_matrix", "_format_factory", "_write_factory"]

    def __init__(self, matrix: ABCMinimalMatrix, format_factory: ABCFormatFactory, write_factory: ABCWriteFactory) -> None:
        self._matrix = matrix
        self._format_factory = format_factory
        self._write_factory = write_factory

    def __call__(self) -> None:
        formatter = self._format_factory(matrix=self._matrix)
        writer = self._write_factory(content=formatter())
        writer()
