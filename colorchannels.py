import cv2 as cv   
import numpy as np 


image=cv.imread("Photos/cat.jpg") 
blank=np.zeros(image.shape[:2],"uint8") 

#Splitting images into red, green and blue (dark areas means that pixel doesnt have that colour and vice versa)
b,g,r=cv.split(image)

#Merge them back together
merged=cv.merge([b,g,r])

#Put the colours as their colour ranges instead of grayscale (just put non wanted as blank)
blue=cv.merge([b,blank,blank])


cv.imshow("Merged",merged)
cv.imshow("Blue",b)
cv.imshow("True Blue",blue)
cv.imshow("Green",g)
cv.imshow("Red",r)
cv.waitKey(0)