# Converts all the files in folder path and its subfolders to markdown
import argparse
from pathlib import Path
from codelink.codelink import get_filepaths, get_code, to_markdown, copy_to_clipboard


def parse_args():
    parser = argparse.ArgumentParser(
        prog="codelink_path",
        description="Converts a path to markdown code for an LLM to ingest",
    )
    parser.add_argument('-d', '--directory', default=".",
                        help="The path to the directory where files are located.")
    parser.add_argument('-a', '--allowedtypes', nargs='+', default=[".py"],
                        help="The allowed filetypes to include")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    file_paths = get_filepaths(directory=Path(args.directory), allowed_file_types=args.allowedtypes)
    codes = get_code(file_paths)
    md = to_markdown(codes, Path(args.directory))
    copy_to_clipboard(md)
    print(f"Copied '{Path(args.directory).resolve()}' to Clipboard!")


if __name__ == '__main__':
    main()
