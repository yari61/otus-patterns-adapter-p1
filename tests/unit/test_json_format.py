from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock
from json import dumps

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_sum.output.format import JsonFormat
from matrix_sum.matrix import ABCMinimalMatrix


class Container(DeclarativeContainer):
    config = Configuration(default={"cell": 0.0, "shape": (2 ,2)})
    matrix = Factory(Mock, ABCMinimalMatrix, get_cell=Mock(return_value=config.cell()), get_shape=Mock(return_value=config.shape()))
    formatter = Factory(JsonFormat, matrix=matrix)


class Call(TestCase):
    def test_matrix_formatted_to_json_string_correctly(self):
        container = Container()
        formatter = container.formatter()
        expected_result = dumps([[0.0, 0.0], [0.0, 0.0]])

        matrix = formatter()

        self.assertEqual(matrix, expected_result)

if __name__ == "__main__":
    main()
