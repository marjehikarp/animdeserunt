import os

def convert(file_input: str):
    """
    Convert a file path string to a file object.

    Args:
    file_input (str): The file path string.

    Returns:
    file: The file object.
    """
    if not file_input:
        raise ValueError("File path cannot be empty.")

    if not os.path.exists(file_input):
        raise FileNotFoundError(f"The file {file_input} does not exist.")

    return open(file_input, mode='r', encoding='utf-8')
