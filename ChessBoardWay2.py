import numpy as np
import cv2


height = int(input("Write the height: "))
width = int(input("Write the width: "))
pixnum = int(input("Write the number of pixles: "))
pixSize = int(height/pixnum)
light = input("Write te light color: ")
color = light
flag = 1






while True:
    myframe = np.zeros([int(height),int(width),3],dtype=np.uint8)
    for i in range(pixnum):
        for j in range(pixnum):
            if flag == 0:
                flag = 1
                continue    
            if flag == 1:
                myframe[pixSize*i:pixSize*(i+1),pixSize*j:pixSize*(j+1)] = color
                flag = 0
        if flag == 1:
            flag = 0
            continue        
        if flag == 0:
            myframe[pixSize*i:pixSize*(i+1),pixSize*j:pixSize*(j+1)] = color
            flag = 1   
    
    cv2.imshow("myframe",myframe)
    if cv2.waitKey(1)& 0xff == ord('s'):
        break

