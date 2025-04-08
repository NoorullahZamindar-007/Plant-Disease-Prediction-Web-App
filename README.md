# Plant-Disease-Prediction-Web-App
Plant Disease Prediction Web App using Flask, and Deep learning 

Uploading your Flask-based **Plant Disease Prediction** app to **GitHub** with a **professional README.md** 🌟

---  

## ✅ Here's a professional, modern `README.md` template just for your project: 

markdown   
# 🌿 Plant Disease Prediction Web App
    
A deep learning-powered web application built with **Flask** that predicts plant diseases from leaf images using a trained Convolutional Neural Network (CNN) model.
       
<br>   

## 📸 Demo

<img src="https://user-images.githubusercontent.com/your-screenshot.gif" alt="App Demo" width="100%"/>

<br>

## 🚀 Features

- Upload plant leaf images and detect diseases in real-time.
- Deep learning model built with TensorFlow/Keras.
- Clean and responsive user interface using HTML & CSS.
- Supports `.jpg`, `.jpeg`, `.png` file uploads.
- Provides prediction result with probability scores (optional).
- Easily extendable to support more plant classes.

<br>

## 🧠 Model Summary

- **Model Type:** CNN
- **Input Shape:** `(256, 256, 3)`    
- **Output:** 3 classes (e.g., Healthy, Disease A, Disease B)
- **Loss Function:** `categorical_crossentropy`         
- **Optimizer:** `Adam (lr=0.0001)`
- **Metrics:** `accuracy`

Trained using image data with **data augmentation** and **validation split**.

<br>

## 📁 Project Structure

    
plant-disease-app/

│
├── app.py                       # Main Flask app
   
├── plant_model.json             # Model architecture
   
├── plant_model.weights.h5       # Model weights

├── requirements.txt             # Python dependencies

├── static/

│   └── Uploaded images

├── templates/

│   └── index.html               # Frontend template

└── README.md                    # This file


<br>

## 🌐 Live Demo

> You can deploy this app on platforms like **Render**, **Heroku**, or **Railway**.

📦 [Deployment Guide](https://github.com/render-examples/flask) (Render)  
🌍 [Live Site](https://your-live-link.com) (if deployed)

<br>

## 🔧 Installation & Usage

### ⚙️ Step 1: Clone the repo
bash
git clone https://github.com/yourusername/plant-disease-app.git
cd plant-disease-app


### 📦 Step 2: Install dependencies
bash
pip install -r requirements.txt


### ▶️ Step 3: Run the app
bash
python app.py


Then open `http://127.0.0.1:5000` in your browser.

---

## 📦 Requirements

- Python 3.7+
- Flask
- TensorFlow / Keras
- NumPy
- Pillow

Install all at once:
bash
pip install -r requirements.txt


---

## 📊 Dataset (Optional)

This project originally used a labeled dataset of leaf images categorized into:
- `Healthy`
- `Early Blight`
- `Late Blight`
> You can use public datasets like [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease) for training your own models.

---

## 🤖 Training Your Own Model

1. Load your dataset and preprocess images (resize, normalize).
2. Build and train a CNN using Keras.
3. Export model using:
   python
   model.to_json()
   model.save_weights('your_model.weights.h5')
   

---

## 🙌 Acknowledgements

- [Keras Documentation](https://keras.io)
- [PlantVillage Dataset](https://www.kaggle.com/emmarex/plantdisease)
- [Flask Web Framework](https://flask.palletsprojects.com)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

> 🔥 Feel free to fork, improve, and contribute to this project!



---

## 📦 Bonus: `requirements.txt`

Include this file to make it easy to install dependencies:

txt
Flask
tensorflow
numpy
Pillow


---
