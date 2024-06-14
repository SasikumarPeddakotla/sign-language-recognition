import math
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
classifier = Classifier("indian_model6.h5","labels.txt")

offset = 20
imgSize=300
counter=0
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
          "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y","Z"]
gesture_labels = ["Bye","Call Me","Good luck","Heart","Hello","Help","I Love You","Me","Movie",
          "Not Okay","Okay","Perfect","Smile","Sorry","Thank You","You"]

while True:
    ret, img = cap.read()
    imageOutput = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        if len(hands) == 1:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            if x - offset >= 0 and y - offset >= 0 and w > 0 and h > 0:
                imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

                imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

                if h > w:
                    k = imgSize / h
                    wCal = math.ceil(k * w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    wGap = math.ceil((imgSize - wCal) / 2)
                    imgWhite[:, wGap:wCal + wGap] = imgResize
                    # prediction, index = classifier.getPrediction(imgWhite)

                else:
                    k = imgSize / w
                    hCal = math.ceil(k * h)
                    imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                    hGap = math.ceil((imgSize - hCal) / 2)
                    imgWhite[hGap:hCal + hGap, :] = imgResize


                prediction, index = classifier.getPrediction(imgWhite)
            # Cropping and resizing the hand image
            # Prediction based on the classifier
            # Displaying prediction if confidence is high
        elif len(hands) >= 2:
            x_min = min(hand['bbox'][0] for hand in hands)
            y_min = min(hand['bbox'][1] for hand in hands)
            x_max = max(hand['bbox'][0] + hand['bbox'][2] for hand in hands)
            y_max = max(hand['bbox'][1] + hand['bbox'][3] for hand in hands)

            x, y, w, h = x_min, y_min, x_max - x_min, y_max - y_min

            imgCrop = img[y_min - offset:y_max + offset, x_min - offset:x_max + offset]

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

            if h > w:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            prediction, index = classifier.getPrediction(imgWhite)
            # Cropping and resizing the hand image
            # Prediction based on the classifier
            # Displaying prediction if confidence is high
        if max(prediction) > 0.95:
            cv2.putText(imageOutput, labels[index], (x, y - 20),
                        cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)

        cv2.imshow("Cropped Image",imgCrop)
        cv2.imshow("Image White", imgWhite)
    cv2.imshow("Image",imageOutput)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break