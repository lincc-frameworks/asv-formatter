import os

from lf_asv_formatter.simple_formatter import SimpleFormatter
from lf_asv_formatter.tabulate_formatter import TabulateFormatter


def test_rewrite_file_simple(
    assert_text_file_matches,
    tmp_path,
    original_output_simple_path,
    expected_output_simple_path,
):
    """Confirm that we write out the file with the expected format using the simple formatter."""
    output_file = os.path.join(tmp_path, "output_file")
    SimpleFormatter(original_output_simple_path, output_file).rewrite_file()
    assert_text_file_matches(output_file, expected_output_simple_path)


def test_rewrite_file_tabulate(
    assert_text_file_matches,
    tmp_path,
    original_output_tabulate_path,
    expected_output_tabulate_path,
):
    """Confirm that we write out the file with the expected GitHub formatting using tabulate."""
    output_file = os.path.join(tmp_path, "output_file")
    TabulateFormatter(original_output_tabulate_path, output_file).rewrite_file()
    assert_text_file_matches(output_file, expected_output_tabulate_path)
