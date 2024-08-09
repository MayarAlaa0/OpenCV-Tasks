import cv2
import numpy as np


def getVal(val):
    global redval
    redval = val
    print (redval)

xpos =0
ypos =0
def getXpos (val):
    global xpos
    xpos = val
    print (xpos)

def getYpos (val):
    global ypos
    ypos = val
    print (ypos)




cv2.namedWindow('trackbar')
cv2.createTrackbar('xpos','trackbar',0,255,getXpos)
cv2.createTrackbar('ypos','trackbar',0,255,getYpos)


while True:
    frame = np.zeros([200,200,3],dtype=np.uint8)
    cv2.imshow('myframe',frame)
    cv2.moveWindow('myframe',xpos,ypos)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cv2.destroyAllWindows()    
