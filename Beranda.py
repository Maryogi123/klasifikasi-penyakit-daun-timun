# page_title: Beranda
# page_icon: 

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Klasifikasi Daun Timun",  # Ini yang muncul di tab browser
    page_icon="🌿",  # Opsional: emoji untuk tab
    layout="centered",
    initial_sidebar_state="expanded"
)

logo = Image.open("logo_ump.png")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(logo)
    

st.title("Klasifikasi Penyakit Daun Tanaman Timun Berbasis Convolutional Neural Network (CNN)")
st.write("Aplikasi ini mengklasifikasikan penyakit daun timun dengan model CNN berbasis VGG16.")

st.write("""
Tanaman timun rentan terhadap berbagai penyakit daun. Aplikasi ini mengenali 5 jenis kategori penyakit:
""")

st.markdown("""
1. **Bacterial Leaf Spot (Daun Bakteri)**  
2. **Downy Mildew (Embun Bulu)**  
3. **Healthy Leaf (Daun Sehat)**  
4. **Mosaic Disease (Penyakit Mosaik)**  
5. **Powdery Mildew (Embun Tepung)**  
""")

cols1 = st.columns(3)
image_paths1 = [
    ("Bacterial Leaf Spot", "gambar_timun/bacterial_leaf_spot.jpg"),
    ("Downy Mildew", "gambar_timun/downy_mildew.jpg"),
    ("Healthy Leaf", "gambar_timun/healthy_leaf.jpg")
]

for col, (label, path) in zip(cols1, image_paths1):
    with col:
        st.image(path, caption=label, use_container_width=True)

cols2 = st.columns(2)
image_paths2 = [
    ("Mosaic Disease", "gambar_timun/mosaic_disease.jpg"),
    ("Powdery Mildew", "gambar_timun/powdery_mildew.jpg")
]

for col, (label, path) in zip(cols2, image_paths2):
    with col:
        st.image(path, caption=label, use_container_width=True)
