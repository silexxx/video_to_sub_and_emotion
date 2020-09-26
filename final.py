import cv2
import numpy as np

import os
from keras.models import model_from_json
from keras.preprocessing import image

model = model_from_json(open("fer.json", "r").read())
#load weights
model.load_weights('fer.h5')


face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def most_frequent(List): 
    return max(set(List), key = List.count)










cap = cv2.VideoCapture("data/input.mp4")

if (cap.isOpened() == False): 

  print("Unable to read camera feed")


frame_width = int(cap.get(3))

frame_height = int(cap.get(4))

framespersecond= int(cap.get(cv2.CAP_PROP_FPS))

# print("The total number of frames in this video is ", framespersecond)

out = cv2.VideoWriter('output/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), framespersecond, (frame_width,frame_height))

a=[]

while(True):

  ret, test_img = cap.read()

 

  if ret == True:

    gray_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
    

    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)
        roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image
        roi_gray=cv2.resize(roi_gray,(48,48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        #find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]
        a.append(predicted_emotion)

        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        


    # resized_img = cv2(test_img, (420, 420))
    cv2.imshow('Facial emotion analysis ',test_img) 

    out.write(test_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

      break

  else:
    break

emotion=most_frequent(a)
print(emotion)
f = open("emotion/emotion.txt", "w")
f.write(emotion)
f.close()

cap.release()
out.release()
cv2.destroyAllWindows() 
