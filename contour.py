import cv2 as cv 
import numpy as np

#Contours refer to the connecting points of curved lines, whereas edges refer to where a line changes

image=cv.imread("Photos/cat.jpg")

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

#Threshold 1 is lower boundary, 2 is higher boundary
canny=cv.Canny(blur,150,200)

#cv.thresh removes everything that is not within the range, it doesnt find edges, it removes non edges
ret,thresh=cv.threshold(blur,120,220,cv.THRESH_BINARY)

#RETR_LIST determines how the contours are returned (format) , chain approx determines which contours do we want (simple for outline only)
contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

#We can draw these contours as well
blank=np.zeros(image.shape,dtype="uint8")
cv.drawContours(blank,contours,-1,(0,255,0),1)

cv.imshow("Threshold",thresh)
cv.imshow("Drawn contours",blank)

#Tip: Use canny first, second choice use thresholding
cv.waitKey(0)