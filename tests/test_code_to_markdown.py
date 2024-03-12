from codelink.code_to_markdown import get_filepaths, is_directory
from tempfile import TemporaryDirectory
from pathlib import Path


def test_get_filepaths():
    """
    Integration Test for composite get_filepath function
    """
    with TemporaryDirectory() as tmpdir:
        print('created temporary directory', tmpdir)

        Path(tmpdir, 't1.txt').touch()
        Path(tmpdir, 't2.py').touch()
        Path(tmpdir, '.venv').mkdir()
        Path(tmpdir, '.venv/test2.py').touch()
        Path(tmpdir, '__init__.py').touch()

        result = get_filepaths(Path(tmpdir), ['.py'])

        expected_files = {str(Path('t2.py'))}
        actual_files = set([path.name for path in result])

        assert actual_files == expected_files, f'Expected: {expected_files}, got: {actual_files}'


def test_is_directory():
    """
    Test to see if Path is directory
    """
    with TemporaryDirectory() as tmpdir:

        a_file = Path(tmpdir, 'not_a_directory.txt')
        a_directory = Path(tmpdir, 'a_directory')
        a_sub_directory = a_directory / a_directory
        a_sub_file = a_directory / a_file

        a_file.touch()
        assert is_directory(a_file) is False, f"{a_file} is incorrectly classifed as a directory"
        a_directory.mkdir()
        assert is_directory(a_directory) is True, f"{a_directory} is incorrectly classified as NOT a directory"
        a_sub_directory.mkdir(exist_ok=True)
        assert is_directory(a_sub_directory) is True, f"{a_sub_directory} is incorrectly classified as NOT a directory"
        a_sub_file.touch()
        assert is_directory(a_sub_file) is False, f"{a_sub_file} is incorrectly classified as a directory"


