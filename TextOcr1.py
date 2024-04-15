import easyocr
import cv2
# specify languages and other configs
reader = easyocr.Reader(['en'])

# multiple languages (chinese, english)
#reader = easyocr.Reader(['ch_sim','en'])

# no gpu
#reader = easyocr.Reader(['ch_sim','en'], gpu=False)
# image path

image = cv2.imread(r'C:/Users/Admin/PythonLession/TextOCR/text-detection-python-easyocr/data/test1.png') # read image
results = reader.readtext(image)
print(results)
# iterate on all results
for res in results:
    top_left = tuple(res[0][0]) # top left coordinates as tuple
    bottom_right = tuple(res[0][2]) # bottom right coordinates as tuple
    # draw rectangle on image
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    # write recognized text on image (top_left) minus 10 pixel on y
    cv2.putText(image, res[1], (top_left[0]+2, top_left[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("display",image)
cv2.waitKey(0)
cv2.destroyAllWindows()