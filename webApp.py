from flask import Flask, render_template, request, jsonify, url_for
from keras.models import load_model
from keras.utils import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import tensorflow as tf

# Initialize Flask app
app = Flask(__name__)

# Load the trained CNN model
cnn_model = load_model('./model1.h5')  # Update with the path to your trained model

# Define the folder for uploaded images
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Preprocess image function
def preprocess_image(file_path):
    img = load_img(file_path, target_size=(64, 64))  # Resize to model input size
    img = img_to_array(img) / 255.0  # Convert to array and normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img


# Route: Home
@app.route('/')
def index():
    return render_template('index.html')

# Route: Predict
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Save the file to UPLOAD_FOLDER
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Preprocess the image
        img = preprocess_image(file_path)

        # Predict the class
        prediction = cnn_model.predict(img)[0][0]
        result = 'Cancer Detected' if prediction < 0.5 else 'No Cancer Detected'

        # Return the result with the uploaded image URL
        image_url = url_for('static', filename='uploads/' + file.filename)
        return jsonify({'prediction': result, 'image_url': image_url})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Uncomment the following line to train the model
    # train_cnn()
    app.run(debug=True, host='127.0.0.1', port=5001)
