import cv2 as cv 
import numpy as np 

blank=np.zeros((500,500),dtype="uint8")

rectangle=cv.rectangle(blank.copy(),(100,100),(300,500),(255,255,255),-1)
circle=cv.circle(blank.copy(),(200,200),150,(255,255,255),-1)


#Bitwise AND (returns intersection point)
bitwise_and=cv.bitwise_and(rectangle,circle)

#Bitwise OR (returns every pixel)
bitwise_or=cv.bitwise_or(rectangle,circle)

#Bitwise XOR (Non intersecting regions - opposite of and)
bitwise_xor=cv.bitwise_xor(rectangle,circle)

#Bitwise NOT  (Flips black and white)
bitwise_not=cv.bitwise_not(rectangle)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)
cv.imshow("and",bitwise_and)
cv.imshow("or",bitwise_or)
cv.imshow("xor",bitwise_xor)
cv.imshow("Not",bitwise_not)
cv.waitKey(0)