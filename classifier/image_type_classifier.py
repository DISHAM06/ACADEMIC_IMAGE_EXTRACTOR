import cv2
import numpy as np

def load_image(image_path:str):
    img=cv2.imread(image_path)
    return img
def convert_to_grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
def detect_edges(gray_img):
   edges=cv2.Canny(gray_img,50,150) 
   return edges


   