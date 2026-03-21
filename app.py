import os
import numpy as np
import cv2 as cv
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

IMG_SIZE = (80, 80)

# same order as training!!
character = [
    "tung tung sahur", "ballerina cappuccina", "cappuccino assassino", "bombardino crocodilo", "tralalero tralala", "tropipera.jpg", "spc .png", "with vignette", "tantangan .png", "enam dan tujuh .png", "67 ", "empanadetta.jpg", "styracomand.jpeg", "hot dog ballom .png", "variant image a1", "capibarussi-sussi .png", "quai vat chuoi co ba canh tay .png", "pollonavale.jpeg", "la supreme sign combinazione woooooooooooooooooooooooooooow                         ", "shimpanzè piprac un umhracnew.jpg", "trrs.jpg", "reg reg reg sound horeg .png", "bukan.jpeg", "noooo my catfood .jpg", "crocodillo cocosino bombardetto cococosetto.jpg", "pipi panchito.jpg", "71 .png", "tung tung tung sahur .png", "babytoilets.jpg", "steal a brainrot", "p1", "la karkerkar combinasion.webp", "carrotini octopussini .png", "washero dryero.jpg", "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я сахур .png", "bananini pervertini.jpg", "skull .png", "strong strawberry .png", "bunny crab.png", "iconic", "1 1 v1", "catcoconut.webp", "buff bee.png", "1767545045935 .png", "los ynysoedd .png", "ai version", "fox.jpg", "og", "s o f a s o f a.jpg", "opowaekarkerkur.jpeg"
]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# load model
model = load_model("brainrot_model.keras")

# make uploads folder if it doesn't exist
os.makedirs("uploads", exist_ok=True)

# -----------------------------
# preprocess
# -----------------------------
def prepare(img_path):
    img = cv.imread(img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, IMG_SIZE)
    img = img / 255.0
    img = img.reshape(-1, IMG_SIZE[0], IMG_SIZE[1], 1)
    return img

# -----------------------------
# routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            img = prepare(filepath)
            preds = model.predict(img)

            character_index = np.argmax(preds[0])
            prediction = character[character_index]

    return render_template("index.html", prediction=prediction)

# -----------------------------
# run
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)