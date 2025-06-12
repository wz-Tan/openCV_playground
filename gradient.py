import cv2 as cv 
import numpy as np 

#Edge Detection  - sobel (one dimension), laplacian (2d - general purpose), canny - slow but powerful
image=cv.imread("Photos/cat.jpg")
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#Laplacian method
#Use laplacian to calculate the points where edges meet, which can be negative
lap=cv.Laplacian(gray, cv.CV_64F)

#Make numbers positive, limit to within 255
lap=np.uint8(np.absolute(lap))

cv.imshow("Laplacian",lap)

#Sobel (Calculates the edges of one axis at a time)
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined=cv.bitwise_or(sobelx,sobely)

cv.imshow("x",sobelx)
cv.imshow("y",sobely)
cv.imshow("combined",combined)

cv.waitKey(0)