import math
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

offset = 20
imgSize = 300
counter = 0

while True:
    ret, img = cap.read()
    hands, img = detector.findHands(img)

    if len(hands)==1:
        hand = hands[0]
        x,y,w,h=hand['bbox'] # Boundary box around the hand
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

        if h>w:
            k=imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize))
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("Cropped Image",imgCrop)
        cv2.imshow("Image White", imgWhite)

    if len(hands) == 2:
        x_min = min(hand['bbox'][0] for hand in hands)
        y_min = min(hand['bbox'][1] for hand in hands)
        x_max = max(hand['bbox'][0] + hand['bbox'][2] for hand in hands)
        y_max = max(hand['bbox'][1] + hand['bbox'][3] for hand in hands)

        imgCrop = img[y_min - offset:y_max + offset, x_min - offset:x_max + offset]

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        x, y, w, h = x_min, y_min, x_max - x_min, y_max - y_min

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

        # imgResize = cv2.resize(imgCrop, (imgSize, imgSize))
        # imgWhite[:imgResize.shape[0], :imgResize.shape[1]] = imgResize

        cv2.imshow("Cropped Image", imgCrop)
        cv2.imshow("Image White", imgWhite)


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    folder = "Indian_alphabets/Z"
    if key == ord("c"):
        counter += 1
        cv2.imwrite(f'{folder}/img_{counter}.jpg', imgWhite)
        print(counter)

    elif key == ord("q"):
        break

cv2.destroyAllWindows()
