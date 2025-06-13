import cv2 as cv 
#Face detection looks for the edges, regardless of colour
image=cv.imread("Photos/face2.jpeg")

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)


#haar cascade is a prebuilt image classifier by openCV
haar_cascade=cv.CascadeClassifier('haar_face.xml')

#neighbours = how many edges needed to be recognised as a face (min neighbour is a sensitivity setting)
faces_rect=haar_cascade.detectMultiScale(gray,1.1,minNeighbors=3)

#How many faces in image
print(len(faces_rect))

#Draw the rectangle
for (x,y,w,h) in faces_rect:
    cv.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),1)
    
cv.imshow("Gray",gray)
cv.waitKey(0)