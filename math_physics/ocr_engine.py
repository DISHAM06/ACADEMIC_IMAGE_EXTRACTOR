import cv2
import pytesseract


def extract_text_tesseract(image_path: str) -> str:
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    config = r"--oem 3 --psm 6"
    return pytesseract.image_to_string(gray, config=config).strip()
