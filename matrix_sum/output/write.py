from __future__ import annotations
from os import PathLike
from abc import ABC, abstractmethod


class ABCWrite(ABC):
    @abstractmethod
    def __call__(self) -> None:
        pass


class FileWrite(ABCWrite):
    __slots__ = ["_path", "_content"]

    def __init__(self, path: PathLike, content: str) -> None:
        self._path = path
        self._content = content

    def __call__(self) -> None:
        with open(self._path, mode="w") as output_file:
            output_file.write(self._content)


class ABCWriteFactory(ABC):
    @abstractmethod
    def __call__(self, content: str) -> ABCWrite:
        pass


class FileWriteFactory(ABCWriteFactory):
    __slots__ = ["_path"]

    def __init__(self, path: PathLike) -> None:
        self._path = path

    def __call__(self, content: str) -> ABCWrite:
        return FileWrite(path=self._path, content=content)
