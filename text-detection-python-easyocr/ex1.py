import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

#IMAGE_PATH = 'C:/Users/Admin/PythonLession/TextOCR/text-detection-python-easyocr/data/test2.png'


IMAGE_PATH = r'C:\Users\Admin\PythonLession\CarPlate\CropImg\cropped_img_1.jpg'
reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH,paragraph="False")
print (result)