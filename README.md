
```markdown
# 🌿 Plant Disease Detection

A deep learning-based web application that detects plant diseases from leaf images using image classification.

The project uses transfer learning with **MobileNetV2** to classify plant leaf images into different disease categories. A **Streamlit** application provides an easy-to-use interface where users can upload a leaf image and receive the predicted disease along with relevant information.

## 🚀 Live Demo

👉 [Open Plant Disease Detection App](https://plant-disease-detection-cs4vtcucupzekqd9mghv97.streamlit.app/)

---

## 📌 Project Overview

Plant diseases can significantly affect crop production and agricultural productivity. Early identification of diseases can help farmers take appropriate action and reduce crop losses.

This project aims to build an automated image-based plant disease detection system using deep learning.

The system:

- Accepts a plant leaf image as input
- Preprocesses the image
- Uses a trained deep learning model for classification
- Predicts the disease category
- Displays disease-related information through a Streamlit interface

---

## 🎯 Objectives

- Detect plant diseases from leaf images.
- Build a multi-class image classification model.
- Apply transfer learning using MobileNetV2.
- Develop an interactive web application using Streamlit.
- Provide disease information along with the prediction.
- Create a practical end-to-end deep learning project.

---

## 🧠 Machine Learning Approach

### Transfer Learning

The project uses **MobileNetV2**, a lightweight convolutional neural network that has been pretrained on ImageNet.

Instead of training a deep neural network completely from scratch, the pretrained model is used as a feature extractor and adapted for plant disease classification.

### Workflow

```text
Leaf Image
    ↓
Image Preprocessing
    ↓
Resize to 224 × 224
    ↓
MobileNetV2
    ↓
Feature Extraction
    ↓
Classification Layer
    ↓
Disease Prediction
    ↓
Disease Information
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| TensorFlow | Deep Learning |
| Keras | Model development |
| MobileNetV2 | Transfer Learning |
| NumPy | Numerical operations |
| Pandas | Data handling |
| Streamlit | Web application |
| JSON | Disease information |
| Git & GitHub | Version control |

---

## 📂 Dataset

The project uses the **PlantVillage** dataset for plant disease image classification.

Dataset:

[PlantVillage Dataset](https://www.tensorflow.org/datasets/catalog/plant_village)

The dataset contains images of plant leaves belonging to multiple plant and disease categories.

---

## 🔄 Project Pipeline

### 1. Data Collection

Plant leaf images are obtained from the PlantVillage dataset.

### 2. Data Preprocessing

Images are:

- Resized to `224 × 224`
- Loaded in batches
- Normalized/preprocessed for the neural network
- Organized into training and validation datasets

### 3. Model Development

MobileNetV2 is used as the base pretrained model.

The classification layer is adapted to predict the required plant disease classes.

### 4. Model Training

The model is trained using the prepared training dataset and evaluated using validation data.

### 5. Model Saving

The trained model is saved as:

```text
plant_disease_model.keras
```

### 6. Web Application

A Streamlit application allows users to upload a leaf image and obtain the model prediction.

---

## 🖥️ Application

The Streamlit application provides:

- Image upload functionality
- Plant leaf image preview
- Disease prediction
- Disease information
- Simple user-friendly interface

---

## 📁 Repository Structure

```text
plant-disease-detection/
│
├── app.py
├── disease_info.json
├── plant_disease_model.keras
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
```

### File Description

| File | Description |
|---|---|
| `app.py` | Streamlit application |
| `disease_info.json` | Disease information used by the application |
| `plant_disease_model.keras` | Trained deep learning model |
| `requirements.txt` | Required Python libraries |
| `.python-version` | Python version configuration |
| `.gitignore` | Files excluded from Git |

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/akashpoojary042-creator/plant-disease-detection.git
```

### 2. Navigate to the project

```bash
cd plant-disease-detection
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Model Details

**Model:** MobileNetV2  
**Approach:** Transfer Learning  
**Task:** Multi-class Image Classification  
**Input:** Plant leaf image  
**Input Size:** 224 × 224 pixels  
**Output:** Predicted plant disease class  

---

## 💡 Key Skills Demonstrated

- Deep Learning
- Computer Vision
- Image Classification
- Transfer Learning
- TensorFlow & Keras
- Model Deployment
- Streamlit
- Data Preprocessing
- Python
- Git & GitHub

---

## 🔮 Future Improvements

- Add more plant and disease categories.
- Improve model accuracy using data augmentation and fine-tuning.
- Display prediction confidence.
- Add multiple image prediction support.
- Improve the user interface.
- Add treatment/recommendation information.
- Deploy the application with a scalable backend.

---

## 👨‍💻 Author

**Akash Poojary**

BSc Data Science Student

GitHub: [akashpoojary042-creator](https://github.com/akashpoojary042-creator)

