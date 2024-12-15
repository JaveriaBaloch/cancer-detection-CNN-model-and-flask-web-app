
# CNN-based Lung Cancer Detector

This project aims to detect lung cancer using a Convolutional Neural Network (CNN) model deployed with Flask. It includes a Jupyter notebook (`lung_cancer_detection.ipynb`) for model training and a Flask app (`webApp.py`) for making predictions. Additionally, an HTML template (`index.html`) is provided for the web interface.

## Model
- The model is trained using the notebook `lung_cancer_detection.ipynb`.
- It uses a CNN architecture to classify CT scan images into two categories: Normal and Cancerous.

## Flask App
- The Flask app (`webApp.py`) serves as the backend for making predictions.
- It loads the trained model and preprocesses images uploaded by users for prediction.
- Predictions are displayed on the web interface.

## Web Interface
- The web interface (`index.html`) allows users to upload CT scan images and receive predictions for lung cancer.
- It provides feedback on the prediction (Normal or Cancerous).

## Setup Instructions

### Step 1: Set up Virtual Environments
1. Intstall virtual environment:
   ```bash
   python3.7 -m pip install virtualenv
```

2. Create a virtual environment for Flask (Python 3.7)
If you're using virtualenv, create a virtual environment with Python 3.7:
```bash 
virtualenv -p python3.7 venv_flask
```

If you're using venv (Python 3.7 is assumed):
```bash
python3.7 -m venv venv_flask
```
3. Activate the virtual environment for Flask:
On Windows:
```bash
venv_flask\Scripts\activate
```
On macOS/Linux:
```bash
source venv_flask/bin/activate
```
4. Install required dependencies for Flask
```bash
pip install -r requirements.txt
```
5. Create a virtual environment for Jupyter (Python 3.10)
```bash
python3.10 -m venv venv_jupyter
```
6. Activate the virtual environment for Jupyter
On Windows:
```bash 
venv_jupyter\Scripts\activate
```
On macOS/Linux:
```bash
source venv_jupyter/bin/activate
```

Install the necessary Jupyter dependencies:
```bash
pip install jupyter
```

###  Step 2: Run the Project:
1. Activate the Flask virtual environment (venv_flask), then run the Flask app:
```bash
python webApp.py
```
The app will be accessible at http://localhost:5000 in your browser.

2. Run the Jupyter Notebook for training the model

Activate the Jupyter virtual environment (venv_jupyter), then start Jupyter Notebook:
```bash 
jupyter notebook lung_cancer_detection.ipynb
```

### Step 3: Model Path
Ensure that the Model.h5 path is correctly specified in webApp.py. If the model file is in a different directory, update the path accordingly.
- download and import the dataset file form [https://1drv.ms/u/c/50f6c2d269b97793/EaXSp2P3LlBOpCR3g6c5xvUB85LXehRC1vLfXgG4vjnuxg?e=DPNu1k](https://1drv.ms/u/c/50f6c2d269b97793/EaXSp2P3LlBOpCR3g6c5xvUB85LXehRC1vLfXgG4vjnuxg?e=DPNu1k) and unzip and bring it under this project
- Install required dependencies: `pip install -r requirements.txt`
- Run the Flask app: `python webApp.py`
- Access the web interface in your browser at `http://localhost:5000`
- Make sure 'Model.h5' path is correct in 'webApp.py'

## Usage
1. Clone the repository: git clone [https://github.com/JaveriaBaloch/cancer-detection-CNN-model-and-flask-web-app.git](https://github.com/JaveriaBaloch/cancer-detection-CNN-model-and-flask-web-app.git)
2. Install required dependencies: pip install -r requirements.txt
3. Run the Flask app: python webApp.py
4. Access the web interface in your browser at http://localhost:5000
5. Make sure 'Model.h5' path is correct in webApp.py.# cancer-detection-CNN-model-and-flask-web-app
