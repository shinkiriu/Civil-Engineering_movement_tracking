# -*- coding: utf-8 -*-

import cv2
import numpy as np

def calOptical(img1, img2, p0, paths):

    # turn RGB image into gray
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # set the arguments of Lucas-Kanade algorithm
    lk_params = dict(winSize=(15, 15),
                     maxLevel=4,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # calculate optical
    p1, status, err = cv2.calcOpticalFlowPyrLK(gray1, gray2, p0, None, **lk_params)
    paths.append(p1)
    
    for i in range(paths[-1].shape[0]):
        x = int(paths[-1][i][0])
        y = int(paths[-1][i][1])
        xy = "%d,%d" % (x, y)
        cv2.circle(img2, (x, y), 5, (0, 255, 0), -1)
        cv2.putText(img2, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255, 255, 255), thickness = 1)

