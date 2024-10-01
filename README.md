# Calculator App

A simple yet powerful command-line and graphical user interface (GUI) calculator built with Python. This calculator supports basic arithmetic operations and additional functionalities such as square root and power calculations. The project demonstrates the use of object-oriented programming and modular design principles.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Additional operations: square root and exponentiation (power).
- User-friendly graphical interface built with Tkinter.
- Input validation and error handling for invalid inputs.
- Modular architecture with separate files for operations, models, and schemas.

### Project Structure

Calculator_app/
│
├── main.py                   # Main entry point of the application
├── crud/
│   ├── __init__.py            # Package initialization
│   ├── calculator_operations.py  # Arithmetic operations (CRUD logic)
├── models/
│   ├── __init__.py            # Package initialization
│   └── operation_model.py     # Data models (optional)
├── schemas/
│   ├── __init__.py            # Package initialization
│   └── operation_schema.py    # Input/output schemas (optional)
└── README.md                  # Documentation (this file)


#### Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

##### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/An-Tony-1/Python-Calculator.git
   cd calculator_app

2. Ensure you have Tkinter installed. It's typically included with standard Python installations.
3. Run the application:
    "python main.py"

##### Usage
- Open the application, and a GUI window will appear.
- Enter your mathematical expression using the buttons provided.
- Press = to calculate the result.
- Use C to clear the input or Exit to close the application.

## Future Enhancements
- Implement additional mathematical functions (e.g., logarithmic, trigonometric functions).
- Add functionality to save and retrieve calculation history.
- Implement a settings feature to customize the user experience.
- Improve the graphical user interface with more advanced design elements.

## Contributing
Contributions are welcome! If you have suggestions for improvements or find any bugs, please create an issue or submit a pull request.

## Enhancements 
Feel free to add any additional features you've implemented or any specific information relevant to your project.


## Author
### Collins Chukwuebuka Anthony
### collinsanthony748@gmail.com
