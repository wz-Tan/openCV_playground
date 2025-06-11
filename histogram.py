import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

#Histograms are graphs that show you the pixel intensity of an image
image=cv.imread("Photos/cat.jpg")
grayscale=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

blank=np.zeros(image.shape[:2],dtype="uint8")
circle=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,255,-1)

#Find intersection point, then we analyse it later
mask=cv.bitwise_and(grayscale,grayscale,mask=circle)


#Image, color channel, mask, number of bins (in this case bins = pixel intensity, so about 20k pixels have 200 pixel intensity)
gray_hist=cv.calcHist([grayscale],[0],mask=mask,histSize=[256],ranges=[0,256])

#Bins REPRESENT COLOURS IN RGB IMAGES, PIXEL INTENSITY IN GRAYSCALE IMAGES
#We guess what an image is based on how similar their colours are
#Use matplotlib to draw the graph
plt.figure()
plt.title(" Histogram")
plt.ylabel("Number of Pixels")
plt.xlabel("Bins")
plt.xlim([0,256])
# plt.plot(gray_hist)


#Colour Histogram (We take histogram for each colour 0=b,1=g,2=r)
#Pixel intensity / bins in this case means how bright they are
colors=('b','g','r')
for i,col in enumerate(colors):
    histogram=cv.calcHist([image],[i],None,[256], [0,256])
    plt.plot(histogram,color=col)
    
   
plt.show()
