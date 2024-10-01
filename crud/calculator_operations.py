import math
from models.operation_model import Operation

def add(x, y):
    operation = Operation(x, y, 'addition')
    return operation.perform_operation()

def subtract(x, y):
    operation = Operation(x, y, 'subtraction')
    return operation.perform_operation()

def multiply(x, y):
    operation = Operation(x, y, 'multiplication')
    return operation.perform_operation()

def divide(x, y):
    operation = Operation(x, y, 'division')
    return operation.perform_operation()

def power(x, y):
    operation = Operation(x, y, 'power')
    return operation.perform_operation()

def square_root(x):
    operation = Operation(x, operation_type='square_root')
    return operation.perform_operation()
