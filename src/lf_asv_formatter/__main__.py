"""Main file to call from command line and GitHub workflows."""
import argparse

from .simple_formatter import SimpleFormatter
from .tabulate_formatter import TabulateFormatter


def parse_asv_version():
    """Parses asv version from command line arguments."""
    parser = argparse.ArgumentParser("lf_asv_formatter")
    parser.add_argument("--asv_version", help="Version of asv", type=str, required=True)
    return parser.parse_args().asv_version


if __name__ == "__main__":
    asv_version = parse_asv_version()
    formatter = SimpleFormatter() if asv_version >= "0.6.0" else TabulateFormatter()
    formatter.rewrite_file()
