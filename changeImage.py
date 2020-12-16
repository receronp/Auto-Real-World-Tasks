#!/usr/bin/env python3
import os
from PIL import Image


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    img_folder = "supplier-data/images"

    for filename in os.listdir(os.path.join(path, img_folder)):
        if filename[0] != "." and "." in filename:
            with Image.open(os.path.join(path, img_folder) + "/" + filename) as img:
                img = (
                    img.resize((600,400))
                    .convert("RGB")
                    .save(
                        os.path.join(path, img_folder) + "/" + filename.replace("tiff", "jpeg"), format="jpeg"
                    )
                )


if __name__ == "__main__":
    main()

