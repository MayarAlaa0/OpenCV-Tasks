import cv2
import numpy as np

myCam = cv2.VideoCapture(0)

width = 500
height = 500
facewidth = 200
faceheight = 200
startrow = (width/2) - (faceheight/2)
endrow = (width/2) + (faceheight/2)

startcol = (height/2) - (facewidth/2)
endcol = (height/2) + (facewidth/2)
myframe = np.zeros([height,width,3],dtype=np.uint8)
while True:
    ignore, frame = myCam.read()
    resizedFrame = cv2.resize(frame,(width,height))
    resizedFrame[int(startrow):int(endrow),int(startcol):int(endcol)]= (0,0,0)
    cv2.imshow("myWin",resizedFrame)
    cv2.moveWindow('myWin',300,300)
    if cv2.waitKey(1) & 0xff == ord('s'):
       break
myCam.release() 