import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
import pickle
import datetime


'''
img = cv2.imread("24.png")
crop_img = img[0:400, 0:640]
crop_img = cv2.resize(crop_img, (80,50))
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
'''


'''
last_time = time.time()
print(last_time)
time.sleep(65)
present_time = time.time()
print(present_time - last_time)
'''


# To load data
with open('training_data15.pkl', 'rb') as f:
    train_data = pickle.load(f)

'''
print("pre del len = {}".format(len(train_data)))
del train_data[6100:-1]
del train_data[-1]
print("post del len = {}".format(len(train_data)))



with open('combat_data9.pkl', 'wb') as f:
    pickle.dump(train_data,f)
    print("dumped data")
'''



img_no = -1
img = train_data[img_no][0]
value = train_data[img_no][1]
print(value)
cv2.imshow('last image', img)


'''

def keys_to_output(keys):
    
    # Convert keys to a ...multi-hot... array

    # [A,W,D] boolean values.
    
    output = [0,0,0]
    
    #if 'W' in keys and 'A' in keys:
    #    output[0] = 1
    #elif 'W' in keys and 'D' in keys:
    #    output[1] = 1
    if 'P' in keys:
        output[0] = 1
    elif 'K' in keys:
        output[1] = 1
    #elif 'D' in keys:
    #    output[4] = 1
    else:
        output[2] = 1
        
    return output

while True:
    keys = key_check()
    output = keys_to_output(keys)
    print(output)
    time.sleep(0.5)

'''


    
