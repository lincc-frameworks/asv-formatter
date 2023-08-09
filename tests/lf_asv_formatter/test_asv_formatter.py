import os

from lf_asv_formatter.asv_formatter import rewrite_file


def test_rewrite_file(assert_text_file_matches, tmp_path, original_output_path, expected_output_path):
    """Confirm that we write out the file with the expected formatting."""

    output_file = os.path.join(tmp_path, "output_file")
    rewrite_file(original_output_path, output_file)

    assert_text_file_matches(output_file, expected_output_path)
