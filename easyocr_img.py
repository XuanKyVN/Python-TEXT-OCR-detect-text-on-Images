import cv2
import matplotlib.pyplot as plt
import easyocr

reader = easyocr.Reader(['en'])
image = cv2.imread('https://8f430952.rocketcdn.me/content/aim.png')
res = reader.readtext('https://8f430952.rocketcdn.me/content/aim.png')
for (bbox, text, prob) in res:
  # unpack the bounding box
  (tl, tr, br, bl) = bbox
  tl = (int(tl[0]), int(tl[1]))
  tr = (int(tr[0]), int(tr[1]))
  br = (int(br[0]), int(br[1]))
  bl = (int(bl[0]), int(bl[1]))
  cv2.rectangle(image, tl, br, (0, 255, 0), 2)
  cv2.putText(image, text, (tl[0], tl[1] - 10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
plt.rcParams['figure.figsize'] = (16,16)
plt.imshow(image)