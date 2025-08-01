from pdf2image import convert_from_path
from pathlib import Path
import os

def pdf_to_images(pdf_path, temp_img_dir="temp_images", dpi=300):
    """
    Converts each page of a PDF to images.
    Returns list of image paths.
    """
    # Create a temporary directory to hold images
    img_dir = Path(temp_img_dir)
    img_dir.mkdir(parents=True, exist_ok=True)

    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=dpi)
    image_paths = []

    for i, img in enumerate(images):
        img_path = img_dir / f"page_{i+1:03}.png"
        img.save(img_path, "PNG")
        image_paths.append(str(img_path))

    return image_paths

def clear_temp_images(temp_img_dir="temp_images"):
    img_dir = Path(temp_img_dir)
    if img_dir.exists():
        for f in img_dir.glob("*.png"):
            f.unlink()
        img_dir.rmdir()
