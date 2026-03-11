# Developer Guide

## Introduction
This guide provides an overview of the Calculator Application's architecture and codebase. It is intended for developers who wish to understand or contribute to the project.

## File Structure
- `app/`: Contains the main application logic.
  - `main.py`: Entry point for the application.
  - `gui.py`: GUI components and logic.
  - `operations.py`: Basic and advanced operations.
  - `matrix_operations.py`: Matrix-specific operations.
- `utils/`: Contains utility functions.
  - `helpers.py`: Helper functions.
  - `error_handling.py`: Error handling logic.
- `tests/`: Contains unit tests.
  - `test_operations.py`: Unit tests for operations.
  - `test_gui.py`: Unit tests for GUI components.
  - `test_matrix.py`: Unit tests for matrix operations.
- `docs/`: Contains documentation.
  - `user_guide.md`: User guide documentation.
  - `developer_guide.md`: Developer guide documentation.

## Dependencies
- Python 3.x
- Libraries: `tkinter`, `numpy`, `scipy`, `matplotlib`, `pytest`

## Running the Application
1. Ensure all dependencies are installed using `pip install -r requirements.txt`.
2. Run the application with `python app/main.py`.

## Testing
- Run unit tests using `pytest tests/`.

## Contributing
- Follow PEP-8 guidelines for code style.
- Ensure all new features are covered by unit tests.
- Update documentation as necessary.