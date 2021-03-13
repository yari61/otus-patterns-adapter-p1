from __future__ import annotations
from abc import ABC, abstractmethod
from os import PathLike
from typing import List, final

from .read import ABCReadFactory
from .parser import ABCParserFactory
from matrix_sum.matrix import ABCMinimalMatrix, ABCMinimalMatrixFactory


@final
class FileLoadMatrices:
    def __init__(self, read_factory: ABCReadFactory, parser_factory: ABCParserFactory, matrix_factory: ABCMinimalMatrixFactory) -> None:
        self._read_factory = read_factory
        self._parser_factory = parser_factory
        self._matrix_factory = matrix_factory

    def __call__(self) -> List[ABCMinimalMatrix]:
        reader = self._read_factory()
        parser = self._parser_factory(content=reader())
        return [self._matrix_factory(matrix_like=matrix_like) for matrix_like in parser()]
