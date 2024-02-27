from codelink.code_to_markdown import get_filepaths
from tempfile import TemporaryDirectory
from pathlib import Path


def test_get_filepaths():
    """
    Tests get_filepaths behavior. Ensures that 
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
