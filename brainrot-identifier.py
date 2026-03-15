import os
import caer
import canara
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
gc collect()
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


#identify which brainrot it is by name
#identify which brainrot u r by image
#


