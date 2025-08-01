import easyocr
from PIL import Image

# Load the OCR reader once (supports GPU if available)
reader = easyocr.Reader(['en'], gpu=True)

def ocr_image(image_path):
    """
    Perform OCR on a single image using EasyOCR and return the extracted text.
    """
    try:
        results = reader.readtext(image_path, detail=0, paragraph=True)
        return "\n".join(results)
    except Exception as e:
        print(f"[ERROR] EasyOCR failed for {image_path}: {e}")
        return ""

def ocr_all_images(image_paths):
    """
    Perform OCR on a list of image paths and return all text combined.
    """
    all_text = []
    for path in image_paths:
        print(f"[OCR] Processing {path}")
        text = ocr_image(path)
        all_text.append(text.strip())
    return "\n\n".join(all_text)
