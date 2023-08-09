"""Main file to call from command line and github workflows."""


from .asv_formatter import rewrite_file

if __name__ == "__main__":

    rewrite_file()
