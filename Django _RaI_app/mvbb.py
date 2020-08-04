import argparse
import imutils
import math
import cv2
import numpy as np
import json
import requests
import calendar
import time
from datetime import datetime


#########################################################################################################
# 
#
#########################################################################################################


INPUT_FILE = "/Users/yatinsatija/Desktop/Nysaatestvideo.mp4" 
OUTPUT_FILE = "hello1.csv"

width = 800
MAX_EMPTY_FRAMES = 10
MIN_CONTOUR = 17500
empty_frame_count = 0
frame_count=0
API_ENDPOINT="http://127.0.0.1:8000/foot/data/"

if __name__ == "__main__":
    camera = cv2.VideoCapture(INPUT_FILE)
    (grabbed, frame) = camera.read()
    frame_count += 1
    
    (H,W) = frame.shape[:2]
    print(H,W)
    
       
    firstFrame = None
 
    # loop over the frames of the video
    while True:
        # grab the current frame and initialize the occupied/unoccupied
        # text
        (grabbed, frame) = camera.read()
        frame_count += 1

        # if the frame could not be grabbed, then we have reached the end
        # of the video
        if not grabbed:
            break

        # convert it to grayscale, and blur it
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # if the first frame is None, initialize it
        if firstFrame is None:
            firstFrame = gray
            
            continue

        # compute the absolute difference between the current frame and
        # first frame
        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # loop over the contours
        # if the contour is too small, ignore it
        
        i = 0
        while i < len(contours):
            if cv2.contourArea(contours[i]) < MIN_CONTOUR:
                contours.pop(i)
            else:   
                i += 1

        data1= {}
        centroid_count = len(contours)        
        for c in contours:
            
            print("Contour Area:", cv2.contourArea(c))
            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            
            startx = x
            starty = y
            endx = w + x
            endy = h + y
            ts = calendar.timegm(time.gmtime())


            dt_object = datetime.fromtimestamp(ts)
            data={"framecount":str(frame_count),
             "startx": str(startx) ,
             "starty": str(starty) ,
             "endx": str(endx) ,
             "endy":str(endy),
             "in_time":str(dt_object)
             }
            
            z = json.dumps(data)
            
    
            r = requests.post(url = API_ENDPOINT, data = z)
            pastebin_url = r.text 
            print("The pastebin URL is:%s"%pastebin_url) 
            

            
            
            fstream = open(OUTPUT_FILE, "a")
            fstream.write(str(frame_count) + "," + str(startx) + "," + str(starty) + "," + str(endx) + "," +str(endy) + "\n")
            fstream.close()
            
            
            
            
        
    # cleanup the camera and close any open windows
    camera.release()

    
