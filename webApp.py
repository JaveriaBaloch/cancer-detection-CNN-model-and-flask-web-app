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

# Define the CNN model architecture for training (if needed)
def create_cnn_model():
    cnn = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return cnn

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

# Training example: Uncomment and adjust paths for training
def train_cnn():
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    test_datagen = ImageDataGenerator(rescale=1./255)

    training_set = train_datagen.flow_from_directory(
        './dataset/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )

    test_set = test_datagen.flow_from_directory(
        './dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )

    # Create and train the CNN
    cnn = create_cnn_model()
    cnn.fit(
        training_set,
        validation_data=test_set,
        epochs=30
    )
    cnn.save('./model.h5')  # Save the trained model for future use

if __name__ == '__main__':
    # Uncomment the following line to train the model
    # train_cnn()
    app.run(debug=True)
