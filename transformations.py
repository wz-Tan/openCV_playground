import cv2 as cv
import numpy as np

image=cv.imread("Photos/cat.jpg")

#Rule of thumb, get dimensions and the transformation matrix (np 32 float for translate, rotate matrix for rotate)
#Use warp affine for final calculation

#Translation
def translate(image,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    # Creates an Array Like This (Multiply first '1' with x, second '1' with y - matrix transformation technique)
    '''
    [ 1  0  x ]
    [ 0  1  y ]
    '''
    dimensions=(image.shape[1],image.shape[0]) #Width and Height
    return cv.warpAffine(image,transMat,dimensions)

#Rotation
def rotate(image,angle,rotationPoint=None):
    width,height=image.shape[1],image.shape[0]
    
    #If no rotation point we just assume as center
    if rotationPoint==None:
        rotationPoint=(width//2,height//2)
    
    rotationMatrix=cv.getRotationMatrix2D(rotationPoint,angle,1)
    return cv.warpAffine(image,rotationMatrix,(width,height))


#Resizing (use inter area for shrinking, cubic or linear for enlarging )
resized=cv.resize(image,(200,200),cv.INTER_AREA)

#Flipping (0 = vertically, 1=horizontally, -0 = both vertical and horizontal)
flip=cv.flip(image,0)

#Cropping
cropped=image[100:300,200:400]

    
cv.imshow("Image",cropped)
cv.waitKey(0)