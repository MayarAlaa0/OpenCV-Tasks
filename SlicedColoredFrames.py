import numpy as np
import cv2
width = 500
height = 500

myframe = np.zeros([height,width,3],dtype=np.uint8)

myframe[0:int(height/2),0:int(width/2)]= (0,0,255)
myframe[0:int(height/2),int(width/2):width]= (0,255,0)
myframe[int(height/2):height,0:int(width/2)] = (255,255,255)
myframe[int(height/2):height,int(width/2):width] = (0,0,0)
while True:
    cv2.imshow("myframe",myframe)
    if cv2.waitKey(1)& 0xff == ord('s'):
        break

