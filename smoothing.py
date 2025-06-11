import cv2 as cv 

image=cv.imread("Photos/image.jpeg")


#Averaging - replaces every pixel with the average intensity of the grid(kernel is a sliding grid) - larger grid, lower average
average=cv.blur(image,(5,5))

#Gaussian blur (keeps center clearer and blurs out the sides) - sigma x = standard deviation
gaussian=cv.GaussianBlur(image,(5,5),0)

#Median Blur (Noise Cleanup)
median=cv.medianBlur(image,5)

#Bilateral Blurring (Most Effective Blur - Retains edges) 
bilateral=cv.bilateralFilter(image,5,15,50)

cv.imshow("Averaged",average)
cv.imshow("Gaussian",gaussian)
cv.imshow("Median",median)
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)