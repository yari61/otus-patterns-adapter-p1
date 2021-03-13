from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .read import ABCReadFactory, FileReadFactory
from .parser import ABCParserFactory, JsonParserFactory
from .load import FileLoadMatrices
from matrix_sum.matrix import MinimalMatrixFactory


class FileLoadContainer(DeclarativeContainer):
    config = Configuration()
    read_factory = Factory(FileReadFactory, path=config.path)
    parser_factory = Factory(JsonParserFactory)
    matrix_factory = Factory(MinimalMatrixFactory)
    loader = Factory(FileLoadMatrices, read_factory=read_factory, parser_factory=parser_factory, matrix_factory=matrix_factory)

__all__ = ["FileLoadContainer", "FileReadFactory", "JsonParserFactory"]
