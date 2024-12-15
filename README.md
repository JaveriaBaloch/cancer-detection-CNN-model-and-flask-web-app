
# CNN-Based Lung Cancer Detector

This project uses a Convolutional Neural Network (CNN) to detect lung cancer, with a Flask-based backend for predictions and a Jupyter notebook for model training. A web interface (`index.html`) enables users to upload CT scan images and receive predictions.

## Model
- The model is trained using the notebook `lung_cancer_detection.ipynb`.
- It uses a CNN architecture to classify CT scan images into two categories: **Normal** and **Cancerous**.

## Flask App
- The Flask app (`webApp.py`) serves as the backend for making predictions.
- It loads the trained model and preprocesses images uploaded by users for prediction.
- Predictions are displayed on the web interface.

## Web Interface
- The web interface (`index.html`) allows users to upload CT scan images and receive predictions for lung cancer.
- It provides feedback on the prediction (Normal or Cancerous).

---

## Setup Instructions

### Step 1: Set Up Virtual Environments

1. **Install virtual environment**:  
   ```bash
   python3.7 -m pip install virtualenv
   ```

2. **Create a virtual environment for Flask (Python 3.7)**  
   If you're using virtualenv:  
   ```bash
   virtualenv -p python3.7 venv_flask
   ```  
   If you're using venv:  
   ```bash
   python3.7 -m venv venv_flask
   ```

3. **Activate the virtual environment for Flask**:  
   On Windows:  
   ```bash
   venv_flask\Scripts\activate
   ```  
   On macOS/Linux:  
   ```bash
   source venv_flask/bin/activate
   ```

4. **Install required dependencies for Flask**:  
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a virtual environment for Jupyter (Python 3.10)**:  
   Open a separate terminal and run:  
   ```bash
   python3.10 -m venv venv_jupyter
   ```

6. **Activate the virtual environment for Jupyter**:  
   On Windows:  
   ```bash
   venv_jupyter\Scripts\activate
   ```  
   On macOS/Linux:  
   ```bash
   source venv_jupyter/bin/activate
   ```

---

### Step 2: Run the Project

1. **Run the Flask App**:  
   In the first terminal, activate the Flask virtual environment (`venv_flask`) and run the Flask app:  
   ```bash
   python webApp.py
   ```  
   The app will be accessible at [http://localhost:5000](http://localhost:5000).

2. **Run the Jupyter Notebook**:  
   In the second terminal, activate the Jupyter virtual environment (`venv_jupyter`) and start Jupyter Notebook:  
   ```bash
   jupyter notebook lung_cancer_detection.ipynb
   ```

---

### Step 3: Model Path

- Ensure that the `Model.h5` path is correctly specified in `webApp.py`.  
- If the model file is in a different directory, update the path accordingly.

---

## Dataset
1. Download and unzip the dataset from [this link](https://1drv.ms/u/c/50f6c2d269b97793/EaXSp2P3LlBOpCR3g6c5xvUB85LXehRC1vLfXgG4vjnuxg?e=DPNu1k).  
2. Place the dataset folder under this project.

---

## Usage

1. Clone the repository:  
   ```bash
   git clone https://github.com/JaveriaBaloch/cancer-detection-CNN-model-and-flask-web-app.git
   ```

2. Install required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:  
   ```bash
   python webApp.py
   ```

4. Access the web interface in your browser at [http://localhost:5000](http://localhost:5000).

5. Ensure that the `Model.h5` path is correct in `webApp.py`.

---

## Repository
GitHub: [cancer-detection-CNN-model-and-flask-web-app](https://github.com/JaveriaBaloch/cancer-detection-CNN-model-and-flask-web-app)

---

## License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software in compliance with the license terms. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
