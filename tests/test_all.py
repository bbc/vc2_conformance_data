import pytest

from vc2_conformance.file_format import read

from vc2_bit_widths.bundle import bundle_index

from vc2_data_tables import QUANTISATION_MATRICES

from vc2_conformance_data import (
    STATIC_FILTER_ANALYSIS_BUNDLE_FILENAME,
    POINTER_SPRITE_FILENAME,
    BERRIES_PICTURE_FILENAME,
    KINGSWOOD_PICTURE_FILENAME,
    TREES_PICTURE_FILENAME,
    NATURAL_PICTURES_FILENAMES,
)


def test_static_filter_analysis_bundle():
    # Bundle file should contain analyses for every transform with a default
    # quantisation matrix; check that here.
    bundle = bundle_index(STATIC_FILTER_ANALYSIS_BUNDLE_FILENAME)

    available = set(
        (
            entry["wavelet_index"],
            entry["wavelet_index_ho"],
            entry["dwt_depth"],
            entry["dwt_depth_ho"],
        )
        for entry in bundle["static_filter_analyses"]
    )

    assert set(QUANTISATION_MATRICES) == available


@pytest.mark.parametrize(
    "filename",
    set(
        [
            POINTER_SPRITE_FILENAME,
            BERRIES_PICTURE_FILENAME,
            KINGSWOOD_PICTURE_FILENAME,
            TREES_PICTURE_FILENAME,
        ]
    )
    | set(NATURAL_PICTURES_FILENAMES),
)
def test_pictures(filename):
    # Should be able to successfully read the file without crashing...
    read(filename)
