import numpy as np
import cv2


height = int(input("Write the height: "))
width = int(input("Write the width: "))
pixnum = int(input("Write the number of pixles: "))
pixSize = int(height/pixnum)
light = input("Write te light color: ")
dark = input("Write te dark color: ")
color = dark





while True:
    
    myframe = np.zeros([int(height),int(width),3],dtype=np.uint8)
    for i in range(pixnum):
        for j in range(pixnum):
            myframe[pixSize*i:pixSize*(i+1),pixSize*j:pixSize*(j+1)] = color
            if color == dark :
                color = light
            else :
                color = dark
        if color == dark:
            color = light
        else:
            color = dark      

    cv2.imshow("myframe",myframe)
    if cv2.waitKey(1)& 0xff == ord('s'):
        break

