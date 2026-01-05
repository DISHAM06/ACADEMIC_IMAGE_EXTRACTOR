# graphs/bar_extractor.py
import cv2
import numpy as np

def extract_bars(image_path: str):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    bars = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if h > 30 and w > 10:  # bar heuristic
            bars.append((x, h))

    bars = sorted(bars, key=lambda b: b[0])

    # Normalize heights
    max_h = max(h for _, h in bars)
    values = [round(h / max_h * 10, 2) for _, h in bars]

    return values
