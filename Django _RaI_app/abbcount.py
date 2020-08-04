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
import sys

#########################################################################################################
# To check if the new centroid lies inside an old rectangle. 
# Returns true and index of rectangle if centroid lies in one of the rectangles else returns false and -1
#
#########################################################################################################

def centroidCheck(rectagleCenterPoint,r):
    i=0
    while i < len(r):
        if (rectangleCenterPoint[0] < r[i][2]) & (rectangleCenterPoint[0] > r[i][0]) & (rectangleCenterPoint[1] > r[i][1]) & (rectangleCenterPoint[1] < r[i][3]):
            return True,i
        else:
            i += 1
    return False,-1


def pop_rect_all(rect):
    print("popallrectangles")
    i=0
    while i < len(rect):
        rect.pop(i)
        i+=1
'''
def Roi(startx,starty,endx,endy,roi_rect):
    if startx > roi_rect[0] & starty > roi_rect[1] & endx < roi_rect[2] & endy < roi_rect[3]:
        return True
    else:
        return False
'''


H=720

MAX_EMPTY_FRAMES = 10
MIN_CONTOUR = 17500
empty_frame_count = 0
frame_count=0
textIn = 0
textOut = 0
rect_count=0
rect=[]
last_frame=0
API_ENDPOINT="http://127.0.0.1:8000/polls/post/"
input="/Users/yatinsatija/Downloads/mysite/hello1.csv"
OUTPUT_FILE="try1.csv"

if __name__ == "__main__":
    
    
    
    with open(input) as openfileobject:
        for line in openfileobject:
            l= line.split(",")
            
            
            
            frame_no = int(l[0])
            startx = int(l[1])
            starty=int(l[2])
            endx=int(l[3])
            endy=int(l[4]) 
            
            
            if (frame_no > last_frame + 10):
                pop_rect_all(rect)
                
            centroidx = (startx + endx) // 2
            centroidy = (starty + endy) // 2
            rectangleCenterPoint = (centroidx, centroidy)
   
            if len(rect) == 0:
                rect.append((startx,starty,endx,endy))
                print(frame_no,"rectangle added", len(rect))
                rect_count += 1
                
                if starty > H//3:
                    textOut += 1
                    print ("textOut ",textOut)
                else:
                    textIn += 1
                    print ("textIn ",textIn)
            
            else:
                found,i = centroidCheck(rectangleCenterPoint,rect)
                if found == True:
                    rect.pop(i)
                    rect.append((startx, starty, endx, endy))
                    
                else:
                    rect.append((startx,starty,endx,endy))
                    print(frame_no,"rectangle added", len(rect))
                    ts = calendar.timegm(time.gmtime())


                    dt_object = datetime.fromtimestamp(ts)
                    
                    
                    if starty > H//3:
                        textOut += 1
                        
                        print ("textOut ",textOut)
                        fstream = open(OUTPUT_FILE, "a")
                        fstream.write(str(textIn) + "," +str(textOut)+","+str(textIn-textOut)+","+str(dt_object)+"\n")
                        fstream.close()
                        
                    else:
                        textIn += 1
                        
                        print ("textIn ",textIn)
                        fstream = open(OUTPUT_FILE, "a")
                        fstream.write(str(textIn) + "," +str(textOut)+","+str(textIn-textOut)+","+str(dt_object)+"\n")
                        fstream.close()
                        
                    in_count=textIn-textOut
                    
                    
                    data={"in_count":str(in_count),
                    "in_time":str(dt_object),
                    
                    }
                    z = json.dumps(data)
            
    
                    r = requests.post(url = API_ENDPOINT, data = z)
                    pastebin_url = r.text 
                    print("The pastebin URL is:%s"%pastebin_url) 
                    
                    #last_frame = frame_no
    
                    print("textIn,textOut",textIn,textOut)
    
        #when inserted rectangles are more than the centroids pop rectangles 
        
                
    