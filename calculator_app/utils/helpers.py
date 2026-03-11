def parse_input(input_string):
    try:
        return eval(input_string)
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")