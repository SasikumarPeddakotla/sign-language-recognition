import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers


images = []
labels = []
def load_images_and_labels(directory):
    label_mapping = {label: index for index, label in enumerate(os.listdir(directory))}
    for label in os.listdir(directory):
        label_directory = os.path.join(directory, label)
        for filename in os.listdir(label_directory):
            image_path = os.path.join(label_directory, filename)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (224, 224))  # Resize images to a consistent size
            images.append(image)
            labels.append(label_mapping[label])
    return np.array(images), np.array(labels)

# Load the collected data
data_directory = 'Indian_alphabets'
images, labels = load_images_and_labels(data_directory)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Normalize pixel values to be between 0 and 1
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Expand dimensions for compatibility with CNN
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# Define the CNN model architecture
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(os.listdir(data_directory)), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_accuracy* 100:.2f}%')

# Save the trained model
model.save('indian_model6.h5')
