import cv2 as cv 

#Threshold makes images into black and white (based on if it is lower or higher than your boundary) - filtering
image=cv.imread("Photos/cat.jpg")

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#Makes a threshold for images below and above 150, yet within 255
#threshold is the minimum value, thresh is the image
#if image is coloured (b,g,r)  - it filters them individually
threshold, thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)

cv.imshow("Threshold",thresh)

#Adaptive Threshold  (Computer finds the suitable value cap - calculates mean of the nearby pixels to decide the value - higher = white, lower = black)
#We use mean to determine the cap, 11 as the kernel size (how big of an area do you want to capture)
#c is the value to reduce from the mean if we think its not bright enough
adaptive_threshold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)

cv.imshow("Adaptive Threshold",adaptive_threshold)

cv.waitKey(0)