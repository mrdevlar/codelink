# Converts an individual script file to markdown
import argparse
from pathlib import Path
from codelink.codelink import get_code, to_markdown, copy_to_clipboard


def parse_args():
    parser = argparse.ArgumentParser(
        prog="codelink_script",
        description="Converts an individual script file to markdown"
    )
    parser.add_argument('-f', '--filepath', required=True, help="The path to a specific file")
    args = parser.parse_args()
    return args


def main():
    # Get command line arguments
    args = parse_args()

    # Process the specified file only
    codes = get_code([Path(args.filepath)])
    md = to_markdown(codes, Path(args.filepath).parent)
    copy_to_clipboard(md)


if __name__ == '__main__':
    main()
