import argparse  # For handling command line arguments.
from pathlib import Path  # Importing the pathlib module.
from pygments.lexers import guess_lexer  # Used to determine programming language from file content.
import pyperclip as pc  # For interacting with clipboard.
from typing import AnyStr  # Type hints for Python's built-in types


def get_filepaths(directory: Path, allowed_file_types: list[str]) -> list[Path]:
    """Return a list of file paths in the given directory that are not directories or special files, have one of the allowed extensions."""
    files = []

    for file in directory.rglob('*'):
        is_file = is_not_directory(file)
        not_namespace = is_not_namespace(file)
        allowed_extension = has_allowed_extension(file, allowed_file_types)
        not_ignored_folder = is_not_ignored_folder(file)

        if is_file and not_namespace and allowed_extension and not_ignored_folder:
            files.append(file)

    return files


def is_not_directory(file: Path) -> bool: 
    """Check if a given file is not a directory."""
    return file.is_file()


def is_not_namespace(file: Path) -> bool: 
    """Check if the filename is a namespace file like __init__.py"""
    return not file.name.startswith("__")


def is_not_ignored_folder(file: Path) -> bool:
    """Check if folder is not to be included, currently only .venv"""
    return not any(path in str(file) for path in [".venv", ".git"])


def has_allowed_extension(file: Path, allowed_file_types: list[str]) -> bool: 
    """Check if the file's extension is one of the allowed ones."""
    return any(extension in allowed_file_types for extension in file.suffixes)


def get_code(files: list[Path]) -> dict[str, str]:
    """Return a dictionary of file paths and their corresponding code snippets."""
    return {str(path): path.read_text(errors='replace') for path in files}


def to_markdown(codes: dict[str, str], directory: Path) -> AnyStr:
    """Return a markdown string of code snippets from the given dictionary."""
    return '\n\n'.join(
        [f"{str(Path(file).relative_to(directory))}\n```{guess_language(code)}\n{code}\n```" for file, code in codes.items()])


def guess_language(content: str) -> str:
    """Return a string describing the programming language present in the content."""
    try:
        return guess_lexer(content).name # noqa
    except Exception as e:
        print(f"Error guessing language for file: {e}")
        return ''


def copy_to_clipboard(markdown: AnyStr) -> None:
    """Copy the given markdown string to clipboard."""
    pc.copy(markdown)