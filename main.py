import tkinter as tk
from tkinter import messagebox
from crud import calculator_operations as calc_ops
from schemas.operation_schema import OperationSchema

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Input field
        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        button_data = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('sqrt', 5, 1), ('^', 5, 2), ('Exit', 5, 3)
        ]

        for (text, row, col) in button_data:
            button = tk.Button(root, text=text, width=10, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)  # Clear the input
        elif char == '=':
            self.calculate()
        elif char == 'Exit':
            self.root.quit()
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + char)

    def calculate(self):
        try:
            expression = self.entry.get()

            # Handle square root operation
            if 'sqrt' in expression:
                number = float(expression.split('sqrt')[1])
                schema = OperationSchema(number, operation_type='square_root')
                is_valid, message = schema.validate()
                if not is_valid:
                    raise ValueError(message)
                result = calc_ops.square_root(number)
            elif '^' in expression:
                base, exp = map(float, expression.split('^'))
                schema = OperationSchema(base, exp, 'power')
                is_valid, message = schema.validate()
                if not is_valid:
                    raise ValueError(message)
                result = calc_ops.power(base, exp)
            else:
                result = eval(expression)

            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
