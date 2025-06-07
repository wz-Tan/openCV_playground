#Rescale/downscale images to save space 

import cv2 as cv

#1 is width, 0 is height
def rescale(frame, scale=0.5):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread("Photos/cat.jpg")
#This works for videos as well, just change the frame to the video's frame
resized_img=rescale(img)

cv.imshow("Image",resized_img)


cv.waitKey(0)

capture=cv.VideoCapture("Videos/doggie---1-minute-video.mp4")
#Change the resolution for live videos
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

