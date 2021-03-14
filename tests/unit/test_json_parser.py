from __future__ import annotations
from unittest import TestCase, main

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_sum.input.parser import JsonParser


class Container(DeclarativeContainer):
    config = Configuration()
    parser = Factory(JsonParser, content=config.content)


class Call(TestCase):
    def test_json_string_parsed_correctly(self):
        container = Container()
        json_string = '{"a": [[0, 0], [0, 0]], "b": [[0, 0], [0, 0]]}'
        container.config.set("content", json_string)
        parser = container.parser()
        expected_result = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]

        matrices = parser()

        self.assertEqual(matrices, expected_result)

if __name__ == "__main__":
    main()
