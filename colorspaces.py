import cv2 as cv 

image=cv.imread("Photos/cat.jpg")

#BGR to Grayscale
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#BGR to HSV (Hue Saturation value) -> Maintains colours even under shadows
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

#BGR TO LAB (mimics how humans perceive colours)
lab=cv.cvtColor(image,cv.COLOR_BGR2LAB)

#BGR TO RGB (Important if you were using other libraries such as matplotlib)
rgb=cv.cvtColor(image,cv.COLOR_BGR2RGB)

cv.imshow("Gray",gray)
cv.imshow("HSV",hsv)
cv.imshow("LAB",lab)
cv.imshow("RGB",rgb)
cv.waitKey(0)