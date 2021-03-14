from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock, patch, call
from os import PathLike

from numpy.typing import ArrayLike
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_sum.input.load import FileLoadMatrices
from matrix_sum.input.read import ABCReadFactory, ABCRead
from matrix_sum.input.parser import ABCParserFactory, ABCParser
from matrix_sum.matrix import ABCMinimalMatrixFactory, ABCMinimalMatrix


class Container(DeclarativeContainer):
    config = Configuration(default={"matrix_count": 2})

    reader = Factory(Mock, ABCRead, return_value=config.content)
    read_factory = Factory(Mock, ABCReadFactory, return_value=reader)

    matrix_like = Factory(Mock, ArrayLike)
    matrix_like_list = Factory(lambda matrix_like_factory, matrix_count: [matrix_like_factory() for i in range(0, matrix_count)], matrix_like.provider, config.matrix_count)
    parser = Factory(Mock, ABCParser, return_value=matrix_like_list)
    parser_factory = Factory(Mock, ABCParserFactory, return_value=parser)

    matrix = Factory(Mock, ABCMinimalMatrix, get_cell=Mock(return_value=config.cell), get_shape=Mock(return_value=config.shape))
    matrix_factory = Factory(Mock, ABCMinimalMatrixFactory, return_value=matrix)

    load = Factory(FileLoadMatrices, read_factory=read_factory, parser_factory=parser_factory, matrix_factory=matrix_factory)


class Call(TestCase):
    def test_parser_created_with_correct_content(self):
        container = Container()
        parser_factory = container.parser_factory()
        loader = container.load(parser_factory=parser_factory)

        loader()

        parser_factory.assert_called_once_with(content=container.config.content())

    def test_matrix_factory_called_with_each_matrix_like(self):
        container = Container()

        matrix_like_list = container.matrix_like_list()
        parser = container.parser(return_value=matrix_like_list)
        parser_factory = container.parser_factory(return_value=parser)

        matrix_factory = container.matrix_factory()
        loader = container.load(parser_factory=parser_factory, matrix_factory=matrix_factory)

        loader()

        matrix_factory.assert_has_calls([call(matrix_like=matrix_like) for matrix_like in matrix_like_list])

if __name__ == "__main__":
    main()
