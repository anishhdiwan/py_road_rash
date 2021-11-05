import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
# from alexnet import alexnet2
from getkeys import key_check
import random

WIDTH = 80
HEIGHT = 50
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'whatever you saved  the trained model as...'
wait_time = 30

w = [0,0,1,0,0]
a = [0,0,0,1,0]
d = [0,0,0,0,1]
wa = [1,0,0,0,0]
wd = [0,1,0,0,0]

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

def right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)
    
def forward_left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
        
def forward_right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)

# model = alexnet2(WIDTH, HEIGHT, LR, output = 5)
# model.load(MODEL_NAME)

def main():
    for i in list(range(wait_time))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # Grabbing the whole screen (1366,786) since compatibility mode runs Road Rash in fullscreen at 640x480
            # Cropping the image to 640x400 to keep final image without speedometer
            screen = grab_screen(region=(0,0,1366,768))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = screen[0:400, 0:640]
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (80,50))

            #prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
            prediction = [0,0,1,0,0]
            print('Prediction: {}'.format(prediction))

            if np.argmax(prediction) == np.argmax(w):
                straight()                
            if np.argmax(prediction) == np.argmax(a):
                left()
            if np.argmax(prediction) == np.argmax(d):
                right()
            if np.argmax(prediction) == np.argmax(wa):
                forward_left()
            if np.argmax(prediction) == np.argmax(wd):
                forward_right()
            
        keys = key_check()
        
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                time.sleep(1)
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

main()       
