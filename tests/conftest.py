import os

import pytest

# pylint: disable=missing-function-docstring, redefined-outer-name

DATA_DIR_NAME = "data"

TEST_DIR = os.path.dirname(__file__)


@pytest.fixture
def test_data_dir():
    return os.path.join(TEST_DIR, DATA_DIR_NAME)


@pytest.fixture
def test_data_simple_dir(test_data_dir):
    return os.path.join(test_data_dir, "simple")


@pytest.fixture
def test_data_tabulate_dir(test_data_dir):
    return os.path.join(test_data_dir, "tabulate")


@pytest.fixture
def assert_text_file_matches():
    def assert_text_file_matches(file_name, golden_file_name):
        """Convenience method to read a text file and compare the contents, line for line.

        When file contents get even a little bit big, it can be difficult to see
        the difference between an actual file and the expected contents without
        increased testing verbosity. This helper compares files line-by-line,
        using the provided strings or regular expressions.

        Notes:
            Because we check strings as regular expressions, you may need to escape some
            contents of `expected_lines`.

        Args:
            expected_lines(:obj:`string array`) list of strings, formatted as regular expressions.
            file_name (str): fully-specified path of the file to read
        """

        assert os.path.exists(golden_file_name), f"file not found [{golden_file_name}]"
        with open(golden_file_name, "r", encoding="utf-8") as metadata_file:
            golden_contents = metadata_file.readlines()

        assert os.path.exists(file_name), f"file not found [{file_name}]"
        with open(file_name, "r", encoding="utf-8") as metadata_file:
            contents = metadata_file.readlines()

        assert len(golden_contents) == len(
            contents
        ), f"files not the same length ({len(contents)} vs {len(golden_contents)})"
        for i, expected in enumerate(golden_contents):
            assert expected == contents[i], (
                f"files do not match at line {i + 1} "
                f"(actual: [{contents[i]}] vs expected: [{expected}])"
            )

        metadata_file.close()

    return assert_text_file_matches
