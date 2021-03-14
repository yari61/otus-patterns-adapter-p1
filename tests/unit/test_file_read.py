from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock, patch
from os import PathLike

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_sum.input.read import FileRead


class Container(DeclarativeContainer):
    config = Configuration()
    reader = Factory(FileRead, path=config.path)


class Call(TestCase):
    def test_read_called_with_correct_path(self):
        container = Container()
        path = Mock(PathLike)
        container.config.set("path", path)
        with patch("matrix_sum.input.read.open") as mock_open:
            reader = container.reader()
            reader()
            mock_open.assert_called_once_with(path, mode="r")

if __name__ == "__main__":
    main()
