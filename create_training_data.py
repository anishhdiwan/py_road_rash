# create_training_data.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
import pickle
import datetime


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [A,W,D] boolean values.
    '''
    output = [0,0,0,0,0]
    
    if 'W' in keys and 'A' in keys:
        output[0] = 1
    elif 'W' in keys and 'D' in keys:
        output[1] = 1
    elif 'W' in keys:
        output[2] = 1
    elif 'A' in keys:
        output[3] = 1
    elif 'D' in keys:
        output[4] = 1
        
    return output

wait_time = 30
recording_time = 180
race_num = int(input("Enter race number: "))
# file_name = 'training_data' + str(race_num) + '.npy'
file_name = 'training_data' + str(race_num) + '.pkl'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main():

    for i in list(range(wait_time))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    print("Recording data")
    
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
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])
            
            # if len(training_data) % 1000 == 0:
                # print(len(training_data))
                # np.save(file_name,training_data)

            # Check if the game has been played for 3mins (avg length of level 1)

            present_time = time.time()
            if present_time - last_time > recording_time:
                print(len(training_data))
                now = datetime.datetime.now()
                print("Data recording finished at {}H, {}M, {}S".format(now.hour, now.minute, now.second))

                # np_training_data = np.asarray(training_data, dtype=object)
                # np.save(file_name,np_training_data)

                # To save data
                with open(file_name, 'wb') as f:
                    pickle.dump(training_data,f)

                # To load data
                #with open(file_name, 'rb') as f:
                    # train_data = pickle.load(f)

                paused = True
                quit()

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
                
if __name__ == '__main__':
    print("Press T to pause/unpause data recording. Program will wait for {}s for the game to start. Recording will last for {}mins".format(wait_time, round(recording_time/60,2)))
    main()

'''
    print("Starting dataset generation code")
    
    file_name = 'training_data.npy'
    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        training_data = list(np.load(file_name))
    else:
        print('File does not exist, starting fresh!')
        training_data = []
        main()

'''
        

    







        
