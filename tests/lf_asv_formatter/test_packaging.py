import lf_asv_formatter


def test_version():
    """Check to see that we can get the package version"""
    assert lf_asv_formatter.__version__ is not None
