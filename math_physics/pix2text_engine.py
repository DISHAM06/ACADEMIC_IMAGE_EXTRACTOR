from pix2text import Pix2Text
import os

_p2t = None

def get_pix2text_model():
    global _p2t
    if _p2t is None:
        _p2t = Pix2Text()
    return _p2t


def image_to_latex_blocks(image_path: str):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    model = get_pix2text_model()
    page = model(image_path)   # returns Page object

    text_blocks = []
    math_blocks = []

    for element in page.elements:
        text = element.text.strip()

        if not text:
            continue

        # Heuristic: isolated math contains $$ or \mathrm or =
        if "$$" in text or "\\mathrm" in text or "=" in text:
            math_blocks.append(text)
        else:
            text_blocks.append(text)

    return {
        "text_blocks": text_blocks,
        "math_blocks": math_blocks
    }
