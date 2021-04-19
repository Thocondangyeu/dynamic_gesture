import cv2 
import numpy as np 
import os 
import argparse 

import glob
import time


#args = argparse.ArgumentParser()
#args.add_argument('--n', type=str,
#                    help='name of new subject')
#args.add_argument("--g" , type = str , help = "name of gesture")

#args = args.parse_args()

#subject_name = args.n
#gesture_name = args.g

#dst = "data/{}/{}/".format(gesture_name, subject_name)

width = 1920
height = 1080
fps = 30

def get_video_infor(capture):
    if capture.isOpened(): 
        # get vcap property 
        width  = capture.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
        # it gives me 0.0 :/
        fps = capture.get(cv2.CAP_PROP_FPS)
    return (int(width), int(height)), int(fps)

cap1 = cv2.VideoCapture(0)

cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)
cap4 = cv2.VideoCapture(3)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cap3.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap4.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap4.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# cap1.set(cv2.cv.CV_CAP_PROP_FPS,fps)
# cap2.set(cv2.cv.CV_CAP_PROP_FPS,fps)
# cap3.set(cv2.cv.CV_CAP_PROP_FPS,fps)
# cap4.set(cv2.cv.CV_CAP_PROP_FPS,fps)



cap4_infor = get_video_infor(cap4)



cap1_infor, cap2_infor, cap3_infor  = get_video_infor(cap1),  get_video_infor(cap2),  get_video_infor(cap3)
print(cap1_infor, cap2_infor  , cap3_infor , cap4_infor)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# out1 = cv2.VideoWriter(dst + 'cam1-{}.avi'.format(1),fourcc, cap1_infor[1], cap1_infor[0])
# out2 = cv2.VideoWriter(dst + 'cam2-{}.avi'.format(2),fourcc, cap2_infor[1], cap2_infor[0])
# out3 = cv2.VideoWriter(dst + 'cam3-{}.avi'.format(3),fourcc, cap3_infor[1], cap3_infor[0])
# out4 = cv2.VideoWriter(dst + 'cam4-{}.avi'.format(4),fourcc, cap4_infor[1], cap4_infor[0])

while(True):
    # Capture frame-by-frame
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret3, frame4 = cap4.read()

    if any((not ret1, not ret2 , not ret3)):
        break

    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2',frame2)
    cv2.imshow('frame3',frame3)
    cv2.imshow("frame4", frame4)
    # out1.write(frame1)
    # out2.write(frame2)
    # out3.write(frame3)
    # out4.write(frame4)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()