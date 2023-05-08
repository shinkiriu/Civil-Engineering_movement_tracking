# -*- coding: utf-8 -*-
import cv2
import numpy as np

p = []
img = np.zeros((512,512,3), np.uint8)

def clickPos(img0):
    
    img = img0
    print('Please click the positions you want to track, press q to quit')
    
    cv2.imshow("image", img)
    #cv2.resizeWindow("image", 800, 600)
    
    while(1):
        cv2.setMouseCallback("image", mouse)
        cv2.imshow('image',img)
        if cv2.waitKey(1) == ord('q'):#按下q退出
            break
    return p
    

def mouse(event, x, y, flags, param):
    global p
    if event == cv2.EVENT_LBUTTONDOWN:
        print('detected you clicked %d, %d' %(x, y))
        p.append([np.float32(x),np.float32(y)])
        
        print(p)
