import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt

IMG_SIZE = (80,80)
channels = 1

char_path = r'/Users/fanglin/Downloads/brainrot_dataset'

char_dict ={}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))

#sort in descending order
char_dict = caer.sort_dict(char_dict, descending=True)
print(char_dict)
#run

#get top charcaters
character = []
count = 0
for i in char_dict:
    characters.append(i[0])
    count+=1
    if count>=10:
        break
print(character)
#run

#create the training data
train = caer.preprocess_from_dir(
    char_path, 
    characters,
    channels=channels, 
    IMG_SIZE=IMG_SIZE, 
    isShuffle=True, 
    verbosity=0)
#run

print(len(train))
#run
plt.figure(figsize(6,6))
plt.imshow(train[0][0], cmap="gray")
plt.show()
#run

featuresSet, labels = caer.spe_train(train,IMG_SIZE=IMG_SIZE)

#normalize the featureset
from tensorflow.keras.utils import to_categorical

featureSet = caer.normalize(featureSet)
labels = to_categorical(labels, len(characters))

x_train, x_val, y_train, y_val = caer.train_val_split(featureSet, labels, val_ratio=.2)

del train
del featureSet
del labels
gc.collect()
#run

BATCH_SIZE = 32
EPOCHS=10

#image data generator
datagen = canaro.generators.imageDataGenerator()
train_gen = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE)

#creating the model
model = canaro.models.createBrainrotModel(IMG_SIZE = IMG_SIZE, channels=channels, output_dims = len(characters), loss='binary_crossentropy', decay=1e-6, learning_rate=.001, momentum=.9, nesterov=True)

model.summary()
#run

#callbacks
from tensorflow.keras.callbacks import LearningrateScheduler
callback_lists = [LearningRateScheduler(canaro.r_schedule)]

training = model.fit(train_gen, steps_per_epoch = len(x_train)//BATCH_SIZE, epochs=EPOCHS, validation_data=(x_val,y_val), validation_steps=len(y.val)//BATCH_SIZE,callbacks=callbacks_listt)
#run

test_path = r'image_file'
img=cv.imread(test_path)

plt.imshow(img)
plt.show

def prepare(img):
    img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img =cv.reside(img, IMG_SIZE)
    img=caer.reshape(img,IMG_SIZE, 1)
    return img

predictions=model.predict(prepare(img))

print(characters[np.argmax(predictions[0])])


#save trained model
model.save("brainrot_model.keras")

#load trained model
# from tensorflow.keras.model import load_model
# model=load_model("brainrot_model.keras")

#take user data base input picture
def get_valid_image_path():
    while True:
        image_path = input("Please enter image path (or q to quit)")
        if image_path.lower() == 'q':
            sys.exit("Program terminated by user.")
        try:
            if not os.path.isfile(image_path):
                print(f"Error: 'image_path' not found or is not a file. Please try again :(")
                continue
            with Image.open(image_path as img):
                print(f"Success: Loaded image of format {img.format}, size {img.size}.")
                return image_path
        except FileNotFoundError:
            print(f"Error: The file '{image_path}' doesn't exist. Please check path and try again.")
        except (IOError, OSError) as e:
            print(f"Error opening image: {e}. Please check it's valid, unbroken img file and try again.")
        except Exception as e:
            print(f"Unexpected error occured: {e}. Please try again!")

if __name__ = "__main__":
    valid_path = get_valid_image_path()
    print(f"\nProceeding with image: {valid_path}")

get_valid_image_path()

#preprocess image the same way as training image
def prepare(img_path):
    img = cv_imread(img_path)

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, IMG_SIZE)

    img = img/ 255.0 #normalize

    img = img.reshape(-1, IMG_SIZE[0], IMG_SIZE[1], 1)
    return img

#predict
img = prepare(image_path)
predictions = model.predict(img)
charcaters_index = np.argmax(prediction[0])
print("Prediction: ", characters[character_index])

#A WEBSITE ATTEMPT
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h>Welcome to Italian Brainrot identifier!</h>"
    return "<p>Please input your brianrot here: </p>"
    user_image = "<input type='file' accept='.jpg,.png,.jpeg'></input>"
    valid_path = user_image


#FINALLY RUN
hello_world()
image_path = input("Enter image path: ")
img = prepare(image_path)
prediction = model.predict(img)
character_index=np.argmax(prediction[0])
print("This brainrot is: ", characters[character_index])
h







#identify which brainrot it is by name
#identify which brainrot u r by image
#


#grrrrrrrrrr