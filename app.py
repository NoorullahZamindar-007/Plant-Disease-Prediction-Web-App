from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load model
with open('plant_model.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('plant_model.weights.h5')

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Labels (modify these to match your training labels)
class_names = ['Disease_A', 'Disease_B', 'Healthy']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join('static', file.filename)
            file.save(filepath)

            # Load and preprocess image
            img = image.load_img(filepath, target_size=(256, 256))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            prediction = model.predict(img_array)
            predicted_class = class_names[np.argmax(prediction)]

            return render_template('index.html', prediction=predicted_class, image=filepath)

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
