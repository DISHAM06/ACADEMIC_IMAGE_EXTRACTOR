# graphs/axis_extractor.py
import cv2
import pytesseract

def extract_axis_labels(image_path: str):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray, config="--psm 6")

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    x_label = lines[-1] if lines else "X"
    y_label = lines[0] if lines else "Y"

    return x_label, y_label
