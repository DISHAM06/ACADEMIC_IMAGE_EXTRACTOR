# graphs/graph_detector.py
import cv2
import numpy as np

def is_bar_chart(image_path: str) -> bool:
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Vertical line density heuristic
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
    vertical_lines = cv2.morphologyEx(edges, cv2.MORPH_OPEN, vertical_kernel)

    score = np.sum(vertical_lines > 0)
    return score > 2000
