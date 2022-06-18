#!/usr/bin/env python3

import pathlib
from PIL import Image

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()
SOURCE_DIR = CURRENT_DIR / 'img/source'
OUTPUT_DIR = CURRENT_DIR / 'img'

def main():
    """Creates resized thumbnail."""
    for image_file in SOURCE_DIR.iterdir():
        if not (OUTPUT_DIR / image_file.name).exists():
            source_image = Image.open(image_file)
            derivative = source_image.copy()
            derivative.thumbnail((700, 700))
            derivative.save(OUTPUT_DIR / image_file.name)

main()
