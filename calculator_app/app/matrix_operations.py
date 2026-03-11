import numpy as np

def perform_matrix_operation(operation, matrix_a, matrix_b=None):
    if operation == 'add':
        return np.add(matrix_a, matrix_b)
    elif operation == 'subtract':
        return np.subtract(matrix_a, matrix_b)
    elif operation == 'multiply':
        return np.dot(matrix_a, matrix_b)
    elif operation == 'determinant':
        return np.linalg.det(matrix_a)
    else:
        raise ValueError("Unknown matrix operation.")