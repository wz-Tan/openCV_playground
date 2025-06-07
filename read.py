import cv2 as cv

# #Read Image
# img=cv.imread("Photos/apple.jpg")

# #Show image
# cv.imshow("Apple Window",img)
# cv.waitKey(0) - plays image forever

#Read Video (Input 0,1,2 ro access webcam or just definite path of file)
vid=cv.VideoCapture("Videos/doggie---1-minute-video.mp4")

#Play Video By Looping over Frames, exit when "d" is pressed
while True:
    isTrue, frame=vid.read() #Returns if the frame is read and the frame itself
    cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF==ord("d"):  #Wait for 20s - becomes true, capture if d is clicked
        break

#Delete the video and all windows once done 
vid.release()
cv.destroyAllWindows()
