import numpy as np
import cv2
import math

# read image
img = cv2.imread(r"C:/Users/Admin/PythonLession/CarPlate/Picture/Bien so o to_102.jpeg")

# change size of image
scale_percent = 200
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)

# 2d to 3d (projection)  , and -> rotation point - center point (origin point)
proj2dto3d = np.array([[1, 0, -img.shape[1] / 2],
                       [0, 1, -img.shape[0] / 2],
                       [0, 0, 0],
                       [0, 0, 1]], np.float32)

# 3d matrixs in  x ,y ,z

'''
 you can remove any matrix if you dont want to rotate around it , so in our case 
 we rotate around y axis only so any line ends with " #0 " we can remove it 
 and the programe will run 

'''
rx = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]], np.float32)  # 0

ry = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]], np.float32)

rz = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]], np.float32)  # 0

trans = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 400],  # 400 to move the image in z axis
                  [0, 0, 0, 1]], np.float32)

proj3dto2d = np.array([[200, 0, img.shape[1] / 2, 0],
                       [0, 200, img.shape[0] / 2, 0],
                       [0, 0, 1, 0]], np.float32)

x = 0.0  # 0
y = 0.0
z = 0.0  # 0

cv2.imshow("img", img)

for i in range(0, 50):
    ax = float(x * (math.pi / 180.0))  # 0
    ay = float(y * (math.pi / 180.0))
    az = float(z * (math.pi / 180.0))  # 0

    rx[1, 1] = math.cos(ax)  # 0
    rx[1, 2] = -math.sin(ax)  # 0
    rx[2, 1] = math.sin(ax)  # 0
    rx[2, 2] = math.cos(ax)  # 0

    ry[0, 0] = math.cos(ay)
    ry[0, 2] = -math.sin(ay)
    ry[2, 0] = math.sin(ay)
    ry[2, 2] = math.cos(ay)

    rz[0, 0] = math.cos(az)  # 0
    rz[0, 1] = -math.sin(az)  # 0
    rz[1, 0] = math.sin(az)  # 0
    rz[1, 1] = math.cos(az)  # 0

    r = rx.dot(ry).dot(rz)  # if we remove the lines we put    r=ry
    final = proj3dto2d.dot(trans.dot(r.dot(proj2dto3d)))

    dst = cv2.warpPerspective(img, final, (img.shape[1], img.shape[0]), None, cv2.INTER_LINEAR
                              , cv2.BORDER_CONSTANT, (255, 255, 255))

    cv2.imshow("dst", dst)

    y = y + 3  # increase y angel by 3

    cv2.waitKey(25)

cv2.waitKey(0)