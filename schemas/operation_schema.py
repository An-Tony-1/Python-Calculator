class OperationSchema:
    def __init__(self, num1, num2=None, operation_type=None):
        self.num1 = num1
        self.num2 = num2
        self.operation_type = operation_type

    def validate(self):
        if self.operation_type not in ['addition', 'subtraction', 'multiplication', 'division', 'power', 'square_root']:
            return False, "Invalid operation type"
        if not isinstance(self.num1, (int, float)):
            return False, "First operand must be a number"
        if self.num2 is not None and not isinstance(self.num2, (int, float)):
            return False, "Second operand must be a number"
        return True, "Valid operation"
