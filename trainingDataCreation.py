# %100 -> 3.x secs
# %1000 -> 33.x secs
# %2000 -> 63 secs
# %1500 -> 50.x secs

import urllib.request as ur
import cv2
import numpy as np
import time


url = 'http://100.66.35.46:8080/shot.jpg' # This value will change

count = 0
i = 0

while True:
    try:
        imgResp=ur.urlopen(url)
    except:
        print("ERROR \n Connection not established")
        break
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    image = cv2.imdecode(imgNp,-1)

    if count%100 == 0 :
        path = "/home/ayush/Desktop/workSpace/TRAIN/train_data{}.png".format(i) # This directory will change as per Raspberry Pi
        i = i+1
        cv2.imwrite(path,image)
        print("Image capture"+" "+str(i))
    if ord('q')==cv2.waitKey(10):
        exit(0)

    count+=1
