import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = tf.keras.models.load_model("plant_disease_model.keras")

# -----------------------------
# Load Disease Information
# -----------------------------
with open("disease_info.json", "r") as file:
    disease_info = json.load(file)

# -----------------------------
# Title
# -----------------------------
st.title("🌿 Plant Disease Detection")
st.write("Upload a leaf image and click Predict.")

# -----------------------------
# Upload Image
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Prediction
# -----------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Resize image
    image = image.resize((160, 160))

    # Convert image to NumPy array
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    predicted_index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100

    disease = disease_info[predicted_index]

    # Display Results
    st.success(f"🌿 Disease: {disease['name']}")

    st.write(f"### 🎯 Confidence: {confidence:.2f}%")

    st.subheader("🦠 Cause")
    st.info(disease["cause"])

    st.subheader("💊 Cure")
    st.success(disease["cure"])