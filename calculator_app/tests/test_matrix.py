import pytest
import numpy as np
from app.matrix_operations import perform_matrix_operation

def test_matrix_operations():
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])

    result_add = perform_matrix_operation('add', matrix_a, matrix_b)
    assert np.array_equal(result_add, np.array([[6, 8], [10, 12]]))

    result_subtract = perform_matrix_operation('subtract', matrix_a, matrix_b)
    assert np.array_equal(result_subtract, np.array([[-4, -4], [-4, -4]]))

    result_multiply = perform_matrix_operation('multiply', matrix_a, matrix_b)
    assert np.array_equal(result_multiply, np.array([[19, 22], [43, 50]]))

    result_determinant = perform_matrix_operation('determinant', matrix_a)
    assert result_determinant == pytest.approx(-2.0, 0.0001)