import pytest
from app.gui import CalculatorGUI
import tkinter as tk

def test_gui_creation():
    root = tk.Tk()
    app = CalculatorGUI(root)
    assert app.master == root
    assert app.result_var.get() == ""