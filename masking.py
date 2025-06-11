import cv2 as cv 
import numpy as np    
#Masking - Mask over important parts and ignore the others


image=cv.imread("Photos/cat.jpg")
blank=np.zeros(image.shape[:2],dtype="uint8")

mask=cv.circle(blank,(image.shape[1]//2,image.shape[0]//2-200),200,255,-1)
cv.imshow("Mask",mask)

rectangle=cv.rectangle(blank.copy(),(100,100),(400,400),255,-1)
funny_mask=cv.bitwise_or(mask,rectangle)

#Only take out the masked section (which is the circle when applied to the image)
masked_image=cv.bitwise_and(image,image,mask=mask)

cv.imshow("Image",masked_image)
cv.waitKey(0)