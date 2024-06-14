import math
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

detector = HandDetector(maxHands=2)
# classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
americanClassifier = Classifier("Model/american_model6.h5", "Model/labels.txt")
indianClassifier = Classifier("Model/indian_model6.h5", "Model/labels.txt")
gestureClassifier = Classifier("Model/gestures_model5.h5", "Model/gesture_labels.txt")

offset = 20
imgSize = 300
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
          "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
gesture_labels = ["Bye", "Call Me", "Good luck", "Heart", "Hello", "Help", "I Love You", "Me", "Movie", "Not Okay",
                  "Okay", "Perfect", "Smile", "Sorry", "Thank You", "You"]


def decode_image(base64_image):
    try:
        image_data = base64.b64decode(base64_image.split(',')[1])
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print(f"Error decoding image: {e}")
        return None


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    received_image = data.get('image')
    sign_type = data.get('sign_type')

    # Convert base64-encoded image data to NumPy array
    img = decode_image(received_image)
    if img is not None:
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

                    else:
                        k = imgSize / w
                        hCal = math.ceil(k * h)
                        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                        hGap = math.ceil((imgSize - hCal) / 2)
                        imgWhite[hGap:hCal + hGap, :] = imgResize

                    if sign_type == 'american':
                        prediction, index = americanClassifier.getPrediction(imgWhite)
                        if not max(prediction) < 0.70:
                            return jsonify({'prediction': labels[index]})
                    elif sign_type == 'indian':
                        prediction, index = indianClassifier.getPrediction(imgWhite)
                        if not max(prediction) < 0.70:
                            return jsonify({'prediction': labels[index]})
                    elif sign_type == 'gesture':
                        prediction, index = gestureClassifier.getPrediction(imgWhite)
                        if not max(prediction) < 0.70:
                            return jsonify({'prediction': gesture_labels[index]})

                else:
                    return jsonify({'prediction': ''})
                # Cropping and resizing the hand image
                # Prediction based on sign type (American, Indian, Gesture)
                # Checking confidence threshold
            elif len(hands) == 2:
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

                if sign_type == 'american':
                    prediction, index = americanClassifier.getPrediction(imgWhite)
                    if not max(prediction) < 0.95:
                        return jsonify({'prediction': labels[index]})
                elif sign_type == 'indian':
                    prediction, index = indianClassifier.getPrediction(imgWhite)
                    if not max(prediction) < 0.95:
                        return jsonify({'prediction': labels[index]})
                elif sign_type == 'gesture':
                    prediction, index = gestureClassifier.getPrediction(imgWhite)
                    if not max(prediction) < 0.95:
                        return jsonify({'prediction': gesture_labels[index]})
                # Cropping and resizing the hand image
                # Prediction based on sign type (American, Indian, Gesture)
                # Checking confidence threshold
        else:
            return jsonify({'prediction': 'no_hands'})
    else:
        return jsonify({'response': 'Error decoding image'}), 400


if __name__ == '__main__':
    app.run(debug=True)
