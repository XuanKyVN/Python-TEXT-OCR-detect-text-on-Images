
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])

#Image("data/test1.png")
output = reader.readtext('C:/Users/Admin/PythonLession/TextOCR/text-detection-python-easyocr/data/test1.png')
print(output)
