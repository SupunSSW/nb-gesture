import cv2
import numpy as np

hand_classifier = cv2.CascadeClassifier('palm_v4.xml')

fcounter = 0

p = {'x':0, 'y':0}

vid = cv2.VideoCapture(0)

while True:


    ret, resized = vid.read()
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)


    hands = hand_classifier.detectMultiScale(gray, 1.04, 5)


    for (x,y,w,h) in hands:
        fcounter += 1

        cv2.rectangle(resized, (x,y), (x+w,y+h), (127,0,255), 2)
        # print("===Hand===")
        # print(x)
        # print(y)
        # print(w)
        # print(h)

        p[fcounter] = {'x':int(x+w/ 2), 'y':int(y+h/2)}

        cv2.circle(resized, (int(x+w/ 2),int(y+h/2)), 3, (0, 255,0) , -1)

    # try:
    if fcounter > 1:
        if p[fcounter]['x'] - p[fcounter-1]['x'] > 30:
            print("Next")
            print(fcounter)
    # except:
    #     pass
    


    cv2.imshow('Face Detection', resized)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

        
cv2.destroyAllWindows()