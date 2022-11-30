from pathlib import Path

import dpcore
import jetraw
import tifffile


def prepare_and_compress(
        input_path: Path, dat_path: Path, cam_id: str, output_directory: Path
):
    assert input_path.exists()
    assert dat_path.exists()
    image = tifffile.imread(input_path)
    dpcore.load_parameters(dat_path)
    dpcore.prepare_image(image, cam_id)
    jetraw.imwrite(Path(output_directory, input_path.name), image)
