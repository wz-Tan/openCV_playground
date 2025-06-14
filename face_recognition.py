import cv2 as cv 
import numpy as np 

#Retrieve data from other files
people=["Ben Afflek","Elton John","Jerry Seinfield","Madonna","Mindy Kaling"]


haar_cascade=cv.CascadeClassifier("haar_face.xml")
features=np.load("features.npy")
labels=np.load("labels.npy")

#Retrieve previous trained model
recogniser=cv.face.LBPHFaceRecognizer_create()
recogniser.read("trained_model.yml")

#Retrieve Image
image=cv.imread("Faces/train/Ben Afflek/3.jpg")
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#Detect the Face
face_rect=haar_cascade.detectMultiScale(gray,1.1,minNeighbors=4)

for (x,y,w,h) in face_rect:
    face_coords=gray[y:y+h,x:x+w]

    #Compares the face coordinates to previously trained images
    #Since we used the indexes as label, we just call it via the array above
    label,confidence=recogniser.predict(face_coords)
    cv.putText(image,f" {people[label]}",(x,y),cv.FONT_HERSHEY_COMPLEX,0.4,255,1)
    cv.rectangle(image,(x,y),(x+w,y+h),255,1)
    cv.imshow("Image",image)
    

    
cv.waitKey(0)