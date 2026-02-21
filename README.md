
# CNN-Based Lung Cancer Detector

This project uses a Convolutional Neural Network (CNN) to detect lung cancer, with a Flask-based backend for predictions and a Jupyter notebook for model training. A web interface (`index.html`) enables users to upload CT scan images and receive predictions.

## Model
- The model is trained using the notebook `lungs_cancer_detection.ipynb`.
- It uses a CNN architecture to classify CT scan images into two categories: **Normal** and **Cancerous**.

## ML Purpose
This machine learning pipeline learns visual patterns in lung CT images to assist with **binary classification** (Normal vs Cancerous). The goal is to provide a fast, reproducible screening signal by mapping image pixels to a cancer probability, which is then surfaced in the Flask web app for user-uploaded scans.

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

> **Important:** Use **two different Python versions**:
> - Flask app: **Python 3.7**
> - Jupyter notebook: **Python 3.10**

1. **Install Python 3.7 and 3.10 (macOS, via pyenv)**:  
   ```bash
   brew install pyenv
   pyenv install 3.7.17
   pyenv install 3.10.13
   
   ```

2. **Create a virtual environment for Flask (Python 3.7)**:  
   ```bash
   pyenv local 3.7.17
   python -m venv venv_flask
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
   pyenv local 3.10.13
   python -m venv venv_jupyter
   ```

6. **Activate the virtual environment for Jupyter**:  
   On Windows:  
   ```bash
   venv_jupyter\Scripts\activate
   ```  
   On macOS/Linux:  
   ```bash
   source venv_jupyter/bin/activate
   pip install jupyter
   ```

---

### Step 2: Run the Project

1. **Run the Flask App**:  
   In the first terminal, activate the Flask virtual environment (`venv_flask`) and run the Flask app:  
   ```bash
   python webApp.py
   ```  
   The app will be accessible at [http://localhost:5001](http://localhost:5001).

2. **Run the Jupyter Notebook**:  

   In the second terminal, activate the Jupyter virtual environment (`venv_jupyter`) and start Jupyter Notebook:  
   ```bash
   jupyter notebook lungs_cancer_detection.ipynb
   ```

---

### Step 3: Model Path

- Ensure that the `model.h5` path is correctly specified in `webApp.py`.  
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

4. Access the web interface in your browser at [http://127.0.0.1:5001](http://127.0.0.1:5001).

5. Ensure that the `model.h5` path is correct in `webApp.py`.

---

## Repository
GitHub: [cancer-detection-CNN-model-and-flask-web-app](https://github.com/JaveriaBaloch/cancer-detection-CNN-model-and-flask-web-app)

---

## License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software in compliance with the license terms. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
