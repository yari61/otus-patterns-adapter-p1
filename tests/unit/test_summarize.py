from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock, call

from numpy import array, zeros
from numpy.testing import assert_array_equal
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from matrix_sum.operations.summarize import Summarize, ABCSummarizePairFactory, ABCSummarize
from matrix_sum.matrix import ABCMinimalMatrix


class Container(DeclarativeContainer):
    config = Configuration(default={"matrix_count": 2})
    matrix = Factory(Mock, ABCMinimalMatrix, get_cell=Mock(return_value=config.cell), get_shape=Mock(return_value=config.shape))
    matrices = Factory(lambda matrix_factory, matrix_count: [matrix_factory() for i in range(0, matrix_count)], matrix.provider, config.matrix_count)
    summarize_pair = Factory(Mock, ABCSummarize, return_value=matrix)
    summarize_pair_factory = Factory(Mock, ABCSummarizePairFactory, return_value=summarize_pair)
    summarize = Factory(Summarize, matrices=matrices, summarize_pair_factory=summarize_pair_factory)


class Call(TestCase):
    def test_summarize_task_created_for_each_matrix(self):
        container = Container()
        matrices = container.matrices()
        summarize_pair = container.summarize_pair()
        summarize_pair_factory = container.summarize_pair_factory(return_value=summarize_pair)
        summarize = container.summarize(matrices=matrices, summarize_pair_factory=summarize_pair_factory)

        summarize()

        summarize_pair_factory.assert_has_calls([call(matrix1=matrices[0], matrix2=matrices[1]), *[call(matrix1=summarize_pair(), matrix2=matrices[i]) for i in range(2, len(matrices))]])

if __name__ == "__main__":
    main()
