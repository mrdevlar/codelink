import argparse
from pathlib import Path
from code_to_markdown import get_filepaths, get_code, to_markdown, copy_to_clipboard

def parse_args():
    parser = argparse.ArgumentParser(
        prog="Code Path to Markdown",
    ) 
    parser.add_argument('-d', '--directory', default=Path.cwd(), help="The path to the directory where files are located.")
    parser.add_argument('-a', '--allowedtypes', nargs='+', default=[".py"], help="The allowed filetypes to include")
    args = parser.parse_args() 
    return args


def main():
    args = parse_args()
    # ignore_dirs = [Path(d) for d in IGNORE_DIRS] # Convert directories to Path objects
    file_paths = get_filepaths(directory=Path(args.directory), allowed_file_types=args.allowedtypes)
    codes = get_code(file_paths)
    md = to_markdown(codes, Path(args.directory))
    copy_to_clipboard(md)


if __name__ == '__main__':
    main()
