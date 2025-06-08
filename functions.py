import cv2 as cv 

image=cv.imread("Photos/cat.jpg")

#Converting Colors
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale",gray)

#Blur (The tuple size is how much you blur the image)
blur=cv.GaussianBlur(image,(5,5),cv.BORDER_DEFAULT)

#Edge Cascade  - Finding the Edges, We can blur the image to reduce noise
edge=cv.Canny(blur,100,100) #Lower threshold = Higher Sensitivity
cv.imshow("Edges",edge)

#Dilate - Highlight the Edges
dilate=cv.dilate(edge,(3,3),iterations=2)

#Erode - Reverse Dilate
erode=cv.erode(dilate,(3,3),iterations=2)

# Resizing - Interpolation is the method used to resize
resized=cv.resize(image,(200,200))
cv.imshow("Resized",resized)

#Cropping
cropped=image[30:300,20:200]
cv.imshow("Cropped",cropped)

cv.waitKey(0)

#So essentially, change color, blur, make edges, enhance or reverse edges, resize and cropping

