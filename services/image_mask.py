import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import math
import base64
class HSV:
    def __init__(self,image_data):
        imgdata = base64.b64decode(image_data)
        self.filename = 'data/image.jpg'  # I assume you have a way of picking unique filenames
        with open(self.filename, 'wb') as f:
            f.write(imgdata)

    def select_color(self,hsv_matrix):
        # cap = cv2.VideoCapture(0)

        # _, frame = cap.read()
        frame=cv2.imread(self.filename)
        print('Shape : ',np.array(frame).shape)
        if np.array(frame).shape[0] >450  or np.array(frame).shape[1]> 450:
            frame=cv2.resize(frame,(450,450))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([hsv_matrix['lh'], hsv_matrix['ls'], hsv_matrix['lv']],dtype="int32")
        print('> ',lower_hsv)
        upper_hsv = np.array([hsv_matrix['uh'], hsv_matrix['us'], hsv_matrix['uv']],dtype="int32")
        print(upper_hsv,' <')
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow('frame', frame)
        # cv2.imshow('mask', mask)
        # cv2.imshow('res', res)
        return res
    # cv2.destroyAllWindows()
    # cap.release()

#
#
# hsv_matrix=dict()
# hsv_matrix['lh'] = 1
# hsv_matrix['ls'] = 2
# hsv_matrix['lv'] = 2
#
# hsv_matrix['uh'] = 255
# hsv_matrix['us'] = 255
# hsv_matrix['uv'] = 255
#
#
# res=select_color('../data/seed1.png',hsv_matrix)
# cv2.imshow('res', res)
# print('res : ',res)