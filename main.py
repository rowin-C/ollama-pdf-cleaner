# main.py

from src.pdf_to_images import pdf_to_images, clear_temp_images
from src.ocr import ocr_all_images
from src.llm_postprocess import clean_text_with_llm
from src.text_to_pdf import save_text_as_pdf

import os

def get_first_pdf_in_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):
            return os.path.join(folder_path, file)
    return None

def main():
    input_folder = "input"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    input_pdf = get_first_pdf_in_folder(input_folder)
    if not input_pdf:
        print("[ERROR] No PDF file found in the 'input' folder.")
        return

    print(f"[INFO] Processing PDF: {input_pdf}")

    print("[STEP 1] Converting PDF to images...")
    image_paths = pdf_to_images(input_pdf)

    print("[STEP 2] Performing OCR...")
    raw_text = ocr_all_images(image_paths)

    print("[STEP 3] Cleaning text with LLM...")
    cleaned_text = clean_text_with_llm(raw_text)

    if cleaned_text:
        output_pdf_path = os.path.join(output_folder, "cleaned_output.pdf")
        save_text_as_pdf(cleaned_text, output_pdf_path)
        print(f"[✅ DONE] Cleaned PDF saved to: {output_pdf_path}")
    else:
        print("[❌ ERROR] LLM failed to clean the text.")

    clear_temp_images()

if __name__ == "__main__":
    main()
