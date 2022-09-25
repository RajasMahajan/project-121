import cv2
import time
import numpy as np

Video1 = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))


cap = cv2.VideoCapture(0)


time.sleep(2)
bg = 0

for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg,axis=1)


while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break 
    img = np.flip(img,axis=1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
frame = cv2.resize(frame,(640,480))
u_black =np.array([0,120,50])
l_black = np.array([10,255,255])
mask_1 = cv2.inRange(hsv , u_black, l_black)



mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
res = cv2.bitwise_and(frame,frame,mask = mask)


f = frame - res
f = np.where(f == 0 ,img, f)