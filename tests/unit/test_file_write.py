from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock, patch
from os import PathLike

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_sum.output.write import FileWrite


class Container(DeclarativeContainer):
    config = Configuration()
    writer = Factory(FileWrite, path=config.path, content=config.content)


class Call(TestCase):
    def test_read_called_with_correct_path(self):
        container = Container()
        path = Mock(PathLike)
        container.config.set("path", path)
        with patch("matrix_sum.output.write.open") as mock_open:
            writer = container.writer()
            writer()
            mock_open.assert_called_once_with(path, mode="w")

if __name__ == "__main__":
    main()
