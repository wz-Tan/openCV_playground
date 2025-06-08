import cv2 as cv
import numpy as np 

#Create an empty image
blank=np.zeros((500,500,3),dtype="uint8")


#Painting the image
# blank[:]=0,255,0

#Applying a certain range to paint
# blank[20:300]=0,255,0


#Draw a rectangle (Target, coordinates, coordinates, color, thickness) -line is same, just use cv.line
cv.rectangle(blank,(10,10),(200,200),(0,244,0),thickness=1)

#Draw a Circle (Target, coordinates, radius, color, thickness)
cv.circle(blank,(100,100),20,(0,244,244),thickness=2)

#Adding text
cv.putText(blank,"This is a word",(100,100),cv.FONT_HERSHEY_SIMPLEX,1.5,(0,211,0),thickness=2)

cv.imshow( "Blank",blank)
cv.waitKey(0)