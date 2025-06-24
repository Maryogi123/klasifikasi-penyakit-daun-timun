import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

import os
import gdown


# Load model dan label
# Cek apakah file model sudah ada
model_path = "vgg16_timun_model_v2.keras"
if not os.path.exists(model_path):
    with st.spinner("🔄 Mengunduh model CNN VGG16 (**129 MB**) untuk klasifikasi daun timun..."):
        file_id = "1C6mMtsdDEx43AHp-8dyxrfrHB9O2IqB0"  # Ganti sesuai ID Google Drive
        url = f"https://drive.google.com/uc?id={file_id}"
        output = model_path
        gdown.download(url, output, quiet=False)
    st.toast("✅ Model berhasil diunduh!")
# Load model
model = load_model(model_path)

class_names = [
    "Bacterial Leaf Spot (Daun Bakteri)",
    "Downy Mildew (Embun Bulu)",
    "Healthy Leaf (Daun Sehat)",
    "Mosaic Disease (Penyakit Mosaik)",
    "Powdery Mildew (Embun Tepung)"
]

# Peta tautan atau pesan untuk setiap kelas
class_info = {
    "Bacterial Leaf Spot (Daun Bakteri)": "🔗 [Info tentang Angular Leaf Spot Disease](https://plantix.net/id/library/plant-diseases/300007/angular-leaf-spot-disease/)",
    "Downy Mildew (Embun Bulu)": "🔗 [Info tentang Downy Mildew of Cucurbits](https://plantix.net/id/library/plant-diseases/100264/downy-mildew-of-cucurbits/)",
    "Healthy Leaf (Daun Sehat)": "✅ Gambar daun timun tampak **sehat**, tidak terdeteksi penyakit.",
    "Mosaic Disease (Penyakit Mosaik)": "🔗 [Info tentang Cucumber Mosaic Virus](https://plantix.net/id/library/plant-diseases/200006/cucumber-mosaic-virus/)",
    "Powdery Mildew (Embun Tepung)": "🔗 [Info tentang Powdery Mildew](https://plantix.net/id/library/plant-diseases/100002/powdery-mildew/)"
}

st.title("Klasifikasi Penyakit Daun Tanaman Timun Berbasis Convolutional Neural Network (CNN)")

uploaded_file = st.file_uploader("Pilih gambar daun timun", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar yang diupload", use_container_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img)
    img_preprocessed = preprocess_input(img_array)
    img_expanded = np.expand_dims(img_preprocessed, axis=0)

    prediction = model.predict(img_expanded)[0]
    confidence = np.max(prediction) * 100
    predicted_class = class_names[np.argmax(prediction)]

    st.markdown(f"### Hasil Klasifikasi: **{predicted_class}**")
    st.markdown(f"### Tingkat Keyakinan: **{confidence:.2f}%**")
    st.info(class_info[predicted_class])
