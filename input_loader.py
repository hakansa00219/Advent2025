from pathlib import Path

def load_input(file_path: str) -> str:
    """Load input data from a file."""
    path = Path(file_path)
    with path.open('r', encoding='utf-8') as file:
        return file.read()