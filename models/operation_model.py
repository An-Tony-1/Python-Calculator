class Operation:
    def __init__(self, num1, num2=None, operation_type=None, result=None):
        self.num1 = num1
        self.num2 = num2
        self.operation_type = operation_type  # e.g., 'addition', 'subtraction', etc.
        self.result = result

    def __repr__(self):
        return f"Operation({self.num1}, {self.num2}, {self.operation_type}, {self.result})"

    def perform_operation(self):
        if self.operation_type == 'addition':
            self.result = self.num1 + self.num2
        elif self.operation_type == 'subtraction':
            self.result = self.num1 - self.num2
        elif self.operation_type == 'multiplication':
            self.result = self.num1 * self.num2
        elif self.operation_type == 'division':
            self.result = self.num1 / self.num2 if self.num2 != 0 else "Division by zero error"
        elif self.operation_type == 'power':
            self.result = self.num1 ** self.num2
        elif self.operation_type == 'square_root':
            self.result = self.num1 ** 0.5
        return self.result
