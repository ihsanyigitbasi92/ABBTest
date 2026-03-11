import pytest
from app.operations import perform_operation, scientific_operations, statistical_operations

def test_perform_operation():
    assert perform_operation("2 + 2") == 4
    assert perform_operation("10 / 2") == 5
    with pytest.raises(ValueError):
        perform_operation("10 / 0")

def test_scientific_operations():
    assert scientific_operations('sin', 0) == 0
    assert scientific_operations('cos', 0) == 1
    with pytest.raises(ValueError):
        scientific_operations('unknown', 0)

def test_statistical_operations():
    data = [1, 2, 3, 4, 5]
    assert statistical_operations(data, 'mean') == 3
    assert statistical_operations(data, 'median') == 3
    assert statistical_operations(data, 'mode') == 1
    assert statistical_operations(data, 'std') == pytest.approx(1.4142, 0.0001)