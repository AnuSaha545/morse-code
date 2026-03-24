from pathlib import Path

def read_file(path: str) -> str:
    """Read content from file."""
    try:
        return Path(path).read_text()
    except Exception as e:
        raise IOError(f"Failed to read file: {e}")

def write_file(path: str, content: str) -> None:
    """Write content to file."""
    try:
        Path(path).write_text(content)
    except Exception as e:
        raise IOError(f"Failed to write file: {e}")