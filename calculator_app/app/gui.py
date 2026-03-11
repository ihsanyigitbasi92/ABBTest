import tkinter as tk
from operations import perform_operation
from matrix_operations import perform_matrix_operation

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator Application")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_display = tk.Entry(self.master, textvariable=self.result_var, state='readonly')
        self.result_display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = perform_operation(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set(f"Error: {e}")
        else:
            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)