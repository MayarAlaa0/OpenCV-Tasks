import cv2
import numpy as np


def getVal(val):
    global redval
    redval = val
    print (redval)

xpos =0
ypos =0
zpos =0
def getbColor (val):
    global xpos
    xpos = val
    print (xpos)

def getYpos (val):
    global ypos
    ypos = val
    print (ypos)

def getZpos (val):
    global zpos
    zpos = val
    print (zpos)


cv2.namedWindow('trackbar')
cv2.createTrackbar('bcolor','trackbar',0,255,getbColor)
cv2.createTrackbar('gcolor','trackbar',0,255,getYpos)
cv2.createTrackbar('rcolor','trackbar',0,255,getZpos)

while True:
    frame = np.zeros([200,200,3],dtype=np.uint8)
    frame[:,:]=(xpos,ypos,zpos)
    cv2.imshow('myframe',frame)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cv2.destroyAllWindows()    
