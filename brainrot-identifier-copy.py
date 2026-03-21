import os
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt
import sys
from PIL import Image

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import LearningRateScheduler

IMG_SIZE = (80, 80)
channels = 1

char_path = r'brainrot_dataset'

# -----------------------------
# Build character dictionary
# -----------------------------
char_dict = {}
for char in os.listdir(char_path):
    full_path = os.path.join(char_path, char)
    if not os.path.isdir(full_path):
        continue
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))

# sort descending
char_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
print(char_dict)

# get top 10
character = []
for i, key in enumerate(char_dict):
    character.append(key)
    if i >= 9:
        break

print(character)

# -----------------------------
# Load training data (REPLACES caer.preprocess_from_dir)
# -----------------------------
data = []
labels = []

for idx, char in enumerate(character):
    folder = os.path.join(char_path, char)
    for img_name in os.listdir(folder):
        path = os.path.join(folder, img_name)
        img = cv.imread(path)

        if img is None:
            continue

        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.resize(img, IMG_SIZE)

        data.append(img)
        labels.append(idx)

#test, give 1 img folders less importance
from collections import Counter

class_counts = Counter(labels)

total = sum(class_counts.values())
class_weight = {}

for i in class_counts:
    # inverse weighting (fewer samples = lower weight)
    class_weight[i] = class_counts[i] / total

data = np.array(data)
labels = np.array(labels)

print(len(data))

plt.figure(figsize=(6, 6))
plt.imshow(data[0], cmap="gray")
plt.show()

# -----------------------------
# Normalize + reshape
# -----------------------------
data = data / 255.0
data = data.reshape(-1, IMG_SIZE[0], IMG_SIZE[1], 1)

labels = to_categorical(labels, len(character))

# train/val split
split = int(len(data) * 0.8)
x_train, x_val = data[:split], data[split:]
y_train, y_val = labels[:split], labels[split:]

gc.collect()

# -----------------------------
# Model (REPLACES canaro model)
# -----------------------------
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(80,80,1)),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),
    Dense(128, activation='relu'),
    Dense(len(character), activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


model.summary()

# -----------------------------
# Train
# -----------------------------
BATCH_SIZE = 32
EPOCHS = 10

training = model.fit(
    x_train, y_train,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=(x_val, y_val),
    class_weight=class_weight
)

# -----------------------------
# Save model
# -----------------------------
model.save("brainrot_model.keras")

# -----------------------------
# Image input
# -----------------------------
def get_valid_image_path():
    while True:
        image_path = input("Please enter image path (or q to quit): ")
        if image_path.lower() == 'q':
            sys.exit("Program terminated.")

        if not os.path.isfile(image_path):
            print("File not found.")
            continue

        try:
            with Image.open(image_path) as img:
                print(f"Loaded {img.format}, size {img.size}")
            return image_path
        except Exception as e:
            print("Error:", e)

# -----------------------------
# Prepare image (FIXED)
# -----------------------------
def prepare(img_path):
    img = cv.imread(img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, IMG_SIZE)
    img = img / 255.0
    img = img.reshape(-1, IMG_SIZE[0], IMG_SIZE[1], 1)
    return img

# -----------------------------
# Predict
# -----------------------------
if __name__ == "__main__":
    image_path = get_valid_image_path()

    img = prepare(image_path)
    predictions = model.predict(img)

    character_index = np.argmax(predictions[0])
    print("Prediction:", character[character_index])

#debug
print("Starting training...")
training = model.fit(
    x_train, y_train,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=(x_val, y_val)
)

print("Training finished.")

print("Saving model...")
model.save("brainrot_model.keras")
print("Model saved successfully!")