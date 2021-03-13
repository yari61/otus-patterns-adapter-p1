from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .dump import MatrixDump
from .write import FileWriteFactory
from .format import JsonFormatFactory


class DumpContainer(DeclarativeContainer):
    config = Configuration()
    write_factory = Factory(FileWriteFactory, path=config.path)
    format_factory = Factory(JsonFormatFactory)
    dumper = Factory(MatrixDump, matrix=config.matrix, write_factory=write_factory, format_factory=format_factory)

__all__ = ["DumpContainer", "FileWriteFactory", "JsonFormatFactory"]
