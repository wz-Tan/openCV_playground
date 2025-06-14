import os 
import cv2 as cv 
import numpy as np


#Get path, iterate through folders, use haar cascade to get the faces, store the face coords and folder label into arrays and feed to the model

people=["Ben Afflek","Elton John","Jerry Seinfield","Madonna","Mindy Kaling"]
dir=r'C:\Users\Wen Zhe\Desktop\Programming Files\OpenCV\Faces\train'

haar_cascade=cv.CascadeClassifier('haar_face.xml')

#All Faces
features=[]

#Attach label to face 
labels=[]


def create_train():
    # 1 person = 1 folder
    for person in people:
        #path is the subfolder after dir (general folder)
        path=os.path.join(dir,person)
        #label is the index of the person's name in the array
        label=people.index(person)
        
        #Grab all images in the subfolder
        for img in os.listdir(path):
            #Get the path of each separate file
            img_path=os.path.join(path,img)
            
            #Process the image, then append the data into the two arrays, one for index another for values
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray,1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces=gray[y:y+h,x:x+w]
                face_resized = cv.resize(faces, (100, 100))
                features.append(face_resized)
                labels.append(label)
                

create_train()


#Convert data into numpy array, which ML models use
features=np.array(features)
labels=np.array(labels)


#Create a face recognition class
face_recogniser= cv.face.LBPHFaceRecognizer_create()
face_recogniser.train(features,labels)

#Give it a path to save and then we can use that model in other projects
face_recogniser.save("trained_model.yml")
np.save("features.npy",features)
np.save("labels.npy",labels)
print("Hello")