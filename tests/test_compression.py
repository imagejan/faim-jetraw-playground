from pathlib import Path

import pytest

from faim_jetraw.io import prepare_and_compress

input_files = [
    "./data/SN61010244_DarkRef_bin4_274MHz_withNoiseFilter.tif",
    "./data/SN61010245_DarkRef_bin4_274MHz_withNoiseFilter.tif"
]

cam_ids = [
    "61010244_274MHz_NF_bin4",
    "61010245_274MHz_NF_bin4"
]

dat_file = "./dat/61010244_61010245_binning.dat"


@pytest.mark.parametrize("input_file", input_files)
@pytest.mark.parametrize("cam_id", cam_ids)
def test_correct_cam_ids(input_file, cam_id, tmp_path):
    prepare_and_compress(Path(input_file), dat_file, cam_id, tmp_path)
    assert Path(tmp_path, Path(input_file).name).exists()
    assert 65000 < Path(tmp_path, Path(input_file).name).stat().st_size < 68000
