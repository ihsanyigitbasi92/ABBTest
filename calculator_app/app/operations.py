import math
import numpy as np
import scipy.stats as stats

def perform_operation(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed.")
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")

def scientific_operations(operation, value):
    if operation == 'sin':
        return math.sin(value)
    elif operation == 'cos':
        return math.cos(value)
    elif operation == 'tan':
        return math.tan(value)
    elif operation == 'log':
        return math.log10(value)
    elif operation == 'ln':
        return math.log(value)
    elif operation == 'exp':
        return math.exp(value)
    else:
        raise ValueError("Unknown scientific operation.")

def statistical_operations(data, operation):
    if operation == 'mean':
        return np.mean(data)
    elif operation == 'median':
        return np.median(data)
    elif operation == 'mode':
        return stats.mode(data)[0][0]
    elif operation == 'std':
        return np.std(data)
    else:
        raise ValueError("Unknown statistical operation.")