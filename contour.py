import cv2 as cv 

#Contours refer to the connecting points of curved lines, whereas edges refer to where a line changes

image=cv.imread("Photos/cat.jpg")

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#Threshold 1 is lower boundary, 2 is higher boundary
canny=cv.Canny(image,150,200)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

cv.imshow("Image",canny)
cv.waitKey(0)