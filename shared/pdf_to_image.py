# shared/pdf_to_image.py

from pdf2image import convert_from_path
import os

def pdf_to_png(pdf_path: str):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    images = convert_from_path(pdf_path)
    png_path = pdf_path.replace(".pdf", ".png")
    images[0].save(png_path, "PNG")

    return png_path
