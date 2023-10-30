import os

from lf_asv_formatter.simple_formatter import SimpleFormatter
from lf_asv_formatter.tabulate_formatter import TabulateFormatter


def get_test_files(folder):
    """Gets test files in folder."""
    original_output = os.path.join(folder, "original_output")
    original_output_verbose = os.path.join(folder, "original_output_verbose")
    expected_output = os.path.join(folder, "expected_output")
    expected_output_verbose = os.path.join(folder, "expected_output_verbose")
    return (
        original_output,
        original_output_verbose,
        expected_output,
        expected_output_verbose,
    )


def test_rewrite_file_simple(assert_text_file_matches, tmp_path, test_data_simple_dir):
    """Confirm that we write out the file with the expected format using the simple formatter."""
    (
        original_output,
        original_output_verbose,
        expected_output,
        expected_output_verbose,
    ) = get_test_files(test_data_simple_dir)
    output_file = os.path.join(tmp_path, "output_file")
    # If the output is non-verbose
    SimpleFormatter(original_output, output_file).rewrite_file()
    assert_text_file_matches(output_file, expected_output)
    # If the output is verbose
    SimpleFormatter(original_output_verbose, output_file).rewrite_file()
    assert_text_file_matches(output_file, expected_output_verbose)


def test_rewrite_file_tabulate(
    assert_text_file_matches, tmp_path, test_data_tabulate_dir
):
    """Confirm that we write out the file with the expected GitHub formatting using tabulate."""
    (
        original_output,
        original_output_verbose,
        expected_output,
        expected_output_verbose,
    ) = get_test_files(test_data_tabulate_dir)
    output_file = os.path.join(tmp_path, "output_file")
    # If the output is non-verbose
    TabulateFormatter(original_output, output_file).rewrite_file()
    assert_text_file_matches(output_file, expected_output)
    # If the output is verbose
    TabulateFormatter(original_output_verbose, output_file).rewrite_file()
    assert_text_file_matches(output_file, expected_output_verbose)
