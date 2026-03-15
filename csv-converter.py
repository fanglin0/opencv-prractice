import os
import cv2 as cv
# import xml.etree.ElementTree as ET
import re
import numpy as py

dataset_path = "/Users/fanglin/Downloads/brainrot_dataset/test"
csv_file = "brainrot_labels.xml"

# root = ET.Element("dataset")

def clean_label(name):
    #remove extension
    name = os.path.splitext(name)[0]

    name = name.replace("_", " ")
    name = re.sub(r"[^\w\s]", "", name)
    name = " ".join(name.split())
    name = re.sub(r"/d+$", "", name)
    return name

#for the 1 pic a folder
for label in os.listdir(dataset_path):
    label_path = os.path.join(dataset_path, label)
    if os.path.isdir(label_path):
        label = clean_label(label)
        print("Label: ", label)
        for filename in os.listdir(label_path):
            if filename.endswith(('.jpg', ".png", ".jpeg", ".webp")):

                # filename = os.path.splitext(file)[0]
                cleaned_name = clean_label(filename)

                print(" Image: ", cleaned_name)
# tree = ET.ElementTree(root)
# tree.write(output_file)

print("XML dataset file created: ", output_file)
print("\n Now labeling imported dataset")

# for multiple imgs per folder
chars = ['ballerina_cappuccina', 'bombardino_crocodilo', 'cappuccino_assassino', 'tralalero_tralala', 'tung_tung_sahur']
DIR = r'/Users/fanglin/Downloads/brainrot_dataset'
excluded_folder = r'/Users/fanglin/Downloads/brainrot_dataset/test'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for title in chars:
        path = os.pathjoin(DIR, title)
        label = chars.index(title)

        for img in os.listdir(path):

            img_path = os.path,join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            features.append(gray)
            labels.append(label)

create_train()
print("training done------")

features = np.array(features, dtype='object')
labels = np.array(labels)

# title = []

# def create_train():
#     for title in chars:
#         path = os.path.join(DIR,title)
#         label = people.index(person)

#         for img in os.listdir(path):
#             img_path = os.path.join(path, img)

#             img_array = cv.imread(img_path)
#             gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

#             faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
#             for (x,y,w,h) in faces_rect:
#                 face_roi = gray[y:y+h, x:x+w]
#                 features.append(faces_roi)
#                 labels.append(label)

# create_train()
# print('Training done----')

# features = np.array(features, dtype='object')
# labels = np.array(labels)

                
# features=[]
# labels=[]

# def create_train():
#     for 



# # for cleaner 1 picture folders
# with open(csv_file, "w", newline="") as file:
#     writer = csv.writer(file)
    
#     # header row
#     writer.writerow(["filename".strip(), "label"])
    
#     for label in os.listdir(dataset_path):
#         label_path = os.path.join(dataset_path, label)

#         if os.path.isdir(label_path):
#             for image in os.listdir(label_path):
#                 if image.lower().endswith(image_extensions):
#                     image_path = os.path.join(label_path, image)
#                     writer.writerow([image_path, label])

# print("CSV file created successfully.")

#for the imported dataset
