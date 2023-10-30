"""Main file to call from command line and GitHub workflows."""
import asv

from .simple_formatter import SimpleFormatter
from .tabulate_formatter import TabulateFormatter

if __name__ == "__main__":
    if asv.__version__ >= "0.6.0":
        SimpleFormatter().rewrite_file()
    else:
        TabulateFormatter().rewrite_file()
