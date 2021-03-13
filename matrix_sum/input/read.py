from __future__ import annotations
from os import PathLike
from abc import ABC, abstractmethod


class ABCRead(ABC):
    @abstractmethod
    def __call__(self) -> str:
        pass


class FileRead(ABCRead):
    __slots__ = ["_path"]

    def __init__(self, path: PathLike) -> None:
        self._path = path

    def __call__(self) -> str:
        with open(self._path, mode="r") as input_file:
            return input_file.read()


class ABCReadFactory(ABC):
    @abstractmethod
    def __call__(self) -> ABCRead:
        pass


class FileReadFactory(ABCReadFactory):
    __slots__ = ["_path"]

    def __init__(self, path: PathLike) -> None:
        self._path = path

    def __call__(self) -> ABCRead:
        return FileRead(path=self._path)
