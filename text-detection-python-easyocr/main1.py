import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
import glob



# read image
path = 'C:/Users/Admin/PythonLession/CarPlate/images/bien_so_xe_may/bien so xe may_8.jpeg'
#for file in glob.glob(path):
img = cv2.imread(path)
#img=cv2.resize(img,(640,400))
    # Detect in a region of picture / Frame
    #img = img[100:400, 0:300]
    #img = cv2.resize(img, (1020, 500))

    # instance text detector
reader = easyocr.Reader(['en'], gpu=True)

    # detect text on image
text_ = reader.readtext(img)

threshold = 0.25
    # draw bbox and text
for t_, t in enumerate(text_):
    print(t)
    bbox, text, score = t
    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()






