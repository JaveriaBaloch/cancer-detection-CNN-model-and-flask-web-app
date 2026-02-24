
# 🩺 CNN-Based Lung Cancer Detector

An end-to-end AI web application that classifies lung CT scan images as **Cancerous** or **Normal** using a trained Convolutional Neural Network (CNN), served through a Flask backend with a clean web interface.

> **GitHub:** [cancer-detection-CNN-model-and-flask-web-app](https://github.com/JaveriaBaloch/cancer-detection-CNN-model-and-flask-web-app)

---

## 🔴 Problem Statement & Motivation

Lung cancer is the **leading cause of cancer-related deaths worldwide**, accounting for more deaths than breast, colon, and prostate cancers combined. Most cases are diagnosed at a late stage because early symptoms are silent and manual CT scan interpretation is time-consuming, expensive, and requires specialist expertise that is not universally accessible.

In under-resourced hospitals, radiologists are scarce and patient backlogs are enormous. There is an urgent need for a **fast, accessible, automated first-pass screening tool** that can flag suspicious CT scans and route them for priority review.

This project uses deep learning to assist — not replace — medical professionals, giving any user or clinician an instant, web-based tool to upload a lung CT scan and receive an AI-generated prediction in seconds.

---

## 💡 How It Works

### ML Pipeline
1. **Dataset**: Labeled lung CT scan images (Normal vs. Cancerous) sourced and preprocessed for training.
2. **Model Architecture**: A CNN built with Keras/TensorFlow, trained in `lungs_cancer_detection.ipynb`. The model learns spatial pixel patterns — nodule shapes, densities, and textures — that distinguish cancerous tissue.
3. **Preprocessing**: Input images are resized to **64×64 pixels**, converted to NumPy arrays, and normalized (pixel values scaled to [0, 1]).
4. **Classification**: The model outputs a single probability score. Values below `0.5` → **"Cancer Detected"**; at or above `0.5` → **"No Cancer Detected"**.
5. **Saved Model**: The trained model is serialized as `model.h5` and loaded at Flask app startup.

### Web Application Flow
1. User visits the interface at `http://localhost:5001` and reads an educational overview of lung cancer.
2. User navigates to the **Cancer Detector** section and uploads a CT scan image.
3. The image is sent via `POST /predict` to the Flask backend.
4. Flask saves the image, preprocesses it, runs inference through the CNN, and returns a JSON result.
5. The result and a preview of the uploaded image are rendered dynamically via JavaScript — no page reload required.

---

## 🛠️ Technologies, Tools & Frameworks

| Layer | Technology |
|---|---|
| **Deep Learning** | TensorFlow 2.x, Keras 2.11 |
| **Model Training** | Jupyter Notebook |
| **Backend** | Python 3.7, Flask 2.2.5 |
| **Image Processing** | Pillow 9.5, NumPy 1.21 |
| **Frontend** | HTML5, Bootstrap 5, Vanilla JavaScript, Font Awesome |
| **Model Serialization** | HDF5 (`model.h5`) via `h5py` 3.8 |
| **Data Science** | scikit-learn 1.0, SciPy 1.7, Matplotlib 3.5 |
| **Visualization / Monitoring** | TensorBoard 2.11 |
| **Environment Management** | Python `venv`, `pyenv` (Python 3.7 for Flask, Python 3.10 for Jupyter) |
| **Version Control** | Git, GitHub |

---

## 👩‍💻 Team

| Name | Role | Contributions |
|---|---|---|
| **Javeria Baloch** | Solo Developer / ML Engineer / Full-Stack | Designed and trained the CNN model, built the Flask REST backend, developed the responsive web interface, integrated the ML inference pipeline end-to-end, wrote documentation and setup instructions |

---

## 📦 Dataset

1. Download and unzip the dataset from [this link](https://1drv.ms/u/c/50f6c2d269b97793/EaXSp2P3LlBOpCR3g6c5xvUB85LXehRC1vLfXgG4vjnuxg?e=DPNu1k).
2. Place the dataset folder under this project directory.

---

## ⚙️ Setup Instructions

> **Important:** Use **two different Python versions**:
> - Flask app → **Python 3.7**
> - Jupyter notebook → **Python 3.10**

### Step 1: Set Up Virtual Environments

1. **Install Python 3.7 and 3.10 (macOS, via pyenv)**:
   ```bash
   brew install pyenv
   pyenv install 3.7.17
   pyenv install 3.10.13
   ```

2. **Create and activate the Flask virtual environment (Python 3.7)**:
   ```bash
   pyenv local 3.7.17
   python -m venv venv_flask
   # macOS/Linux
   source venv_flask/bin/activate
   # Windows
   venv_flask\Scripts\activate
   ```

3. **Install Flask dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create and activate the Jupyter virtual environment (Python 3.10)**:  
   Open a **separate terminal** and run:
   ```bash
   pyenv local 3.10.13
   python -m venv venv_jupyter
   # macOS/Linux
   source venv_jupyter/bin/activate
   # Windows
   venv_jupyter\Scripts\activate
   pip install jupyter
   ```

### Step 2: Run the Project

1. **Run the Flask app** (in the `venv_flask` terminal):
   ```bash
   python webApp.py
   ```
   App will be accessible at [http://localhost:5001](http://localhost:5001).

2. **Run the Jupyter Notebook** (in the `venv_jupyter` terminal):
   ```bash
   jupyter notebook lungs_cancer_detection.ipynb
   ```

### Step 3: Model Path

Ensure the `model.h5` path is correctly specified in `webApp.py`. If the model file is in a different directory, update the path accordingly.

---

## 🖥️ Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/JaveriaBaloch/cancer-detection-CNN-model-and-flask-web-app.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python webApp.py
   ```

4. Open [http://127.0.0.1:5001](http://127.0.0.1:5001) in your browser, upload a CT scan image, and get a prediction.

---

## 🚀 Future Scope & Roadmap

- **Multi-class Classification**: Distinguish between cancer types (Adenocarcinoma, Squamous Cell Carcinoma, SCLC) rather than just binary detection.
- **Grad-CAM Explainability**: Overlay heatmaps on the CT scan to highlight which regions the model flagged as suspicious.
- **DICOM Support**: Accept `.dcm` files — the standard medical imaging format used by hospitals.
- **Confidence Score Display**: Show the model's prediction probability alongside the binary result.
- **Cloud Deployment**: Deploy to Azure App Service or AWS Elastic Beanstalk for public access.
- **Patient History Dashboard**: Add authentication and a history panel to track multiple scans per patient over time.
- **Larger & More Diverse Dataset**: Retrain on a broader dataset to improve generalization across CT scanner manufacturers.

---

## 📄 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software in compliance with the license terms. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
