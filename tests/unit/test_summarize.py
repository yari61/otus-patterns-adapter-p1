from __future__ import annotations
from unittest import TestCase, main
from unittest.mock import Mock

from numpy import array, zeros
from numpy.testing import assert_array_equal

from matrix_sum.operations import Summarize
from matrix_sum.matrix import ABCMatrix


class TestCall(TestCase):
    def test_zero_matrices(self):
        matrix1 = Mock(
            ABCMatrix, get_shape=Mock(return_value=(10, 10)), get_row=Mock(return_value=array([0 for i in range(10)])))
        matrix2 = Mock(
            ABCMatrix, get_shape=Mock(return_value=(10, 10)), get_row=Mock(return_value=array([0 for i in range(10)])))
        operation = Summarize(matrices=[matrix1, matrix2])

        result = operation()

        assert_array_equal(result, zeros(shape=(10, 10)))

if __name__ == "__main__":
    main()
